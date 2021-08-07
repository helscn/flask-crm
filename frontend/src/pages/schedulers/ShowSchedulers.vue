<template>
  <q-page>
    <q-card class="q-ma-lg">
      <q-tabs
        v-model="tab"
        align="left"
        inline-label
        class="bg-grey-4 text-primary shadow-2"
        :breakpoint="300"
      >
        <q-tab name="schedulers" label="计划任务" icon="schedule" />
        <q-tab name="logs" label="任务日志" icon="list_alt" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="schedulers" class="q-gutter-md">
          <q-btn-group rounded push>
            <q-btn
              label="新建任务"
              icon="add_circle_outline"
              @click="$router.push('/schedulers/new')"
              color="primary"
            />
            <q-btn
              label="删除任务"
              :disable="selected.length !== 1"
              rounded
              icon="delete_forever"
              @click="removeJob"
              color="primary"
            />
            <q-btn
              label="暂停运行"
              :disable="selected.length !== 1"
              rounded
              icon="pause"
              @click="pauseJob"
              color="primary"
            />
            <q-btn
              label="恢复运行"
              :disable="selected.length !== 1"
              rounded
              icon="play_arrow"
              @click="resumeJob"
              color="primary"
            />
            <q-btn
              label="刷新任务"
              rounded
              icon="refresh"
              @click="refreshJobs"
              color="primary"
            />
          </q-btn-group>

          <q-table
            ref="schedulers"
            :loading="loading"
            :data="jobs"
            :columns="columns"
            row-key="id"
            selection="single"
            :selected.sync="selected"
            :pagination.sync="pagination"
            :filter="filter"
            :visible-columns="visibleColumns"
            @row-dblclick="showJobCard"
            table-header-class="bg-grey-2"
          >
            <template v-slot:top>
              <q-input
                color="black"
                dense
                debounce="300"
                v-model="filter"
                placeholder="搜索计划任务"
              >
                <template v-slot:prepend>
                  <q-icon name="search" />
                </template>
                <template v-if="filter" v-slot:append>
                  <q-icon
                    name="close"
                    @click="filter = ''"
                    class="cursor-pointer"
                  />
                </template>
              </q-input>
              <q-space />
              <q-select
                v-model="visibleColumns"
                multiple
                outlined
                dense
                options-dense
                display-value="列选择"
                emit-value
                map-options
                :options="columns"
                option-value="name"
                options-cover
                style="min-width: 150px"
              />
            </template>
          </q-table>
        </q-tab-panel>

        <q-tab-panel name="logs">
          <div class="text-h6">Alarms</div>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
    <q-dialog v-model="isShowDetail">
      <q-card class="my-card">
        <q-card-section>
          <div class="row no-wrap items-center">
            <div class="col">
              <q-badge
                class="text-subtitle2"
                color="accent"
                align="middle"
                :label="currentJob.no"
              />
              <span class="q-ml-md text-subtitle1"> {{ currentJob.name }}</span>
            </div>
            <div
              class="col-auto text-grey-6 text-subtitle1 q-pt-none row no-wrap items-center"
            >
              {{ currentJob.spec }}
            </div>
          </div>
        </q-card-section>
        <q-img :src="currentJob.thumbnail" />
        <q-card-section>
          <div class="text-wrapper">{{ currentJob.description }}</div>
        </q-card-section>

        <q-separator />

        <q-card-actions align="right">
          <q-btn v-close-popup flat color="primary" label="关闭" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import { mapState, mapGetters } from "vuex";

export default {
  data() {
    return {
      tab: "schedulers",
      loading: false,
      jobs: [],
      filter: "",
      selected: [],
      pagination: { sortBy: null, descending: false, page: 1, rowsPerPage: 5 },
      columns: [
        {
          name: "id",
          label: "ID",
          align: "left",
          field: row => row.id,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "name",
          label: "任务名称",
          align: "center",
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "func",
          label: "任务模块",
          align: "center",
          field: row => row.func,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "trigger",
          label: "触发器",
          align: "center",
          field: row =>
            row.trigger.type == "date"
              ? "单次任务"
              : row.trigger.type == "interval"
              ? "循环任务"
              : row.trigger.type == "cron"
              ? "定时任务"
              : row.trigger.type,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "start_date",
          label: "开始时间",
          align: "center",
          field: row => row.trigger.start_date,
          format: val => val || "(无)",
          sortable: true
        },
        {
          name: "end_date",
          label: "结束时间",
          align: "center",
          field: row => row.trigger.end_date,
          format: val => val || "(无)",
          sortable: true
        },
        {
          name: "next_run_time",
          label: "下次运行时间",
          align: "center",
          field: row => row.next_run_time,
          format: val => val || "(无)",
          sortable: true
        },
        {
          name: "pending",
          label: "执行中",
          align: "center",
          field: row => row.pending,
          format: row => (row.pending ? "\u2705" : "\u274C"),
          sortable: true
        },
        {
          name: "activated",
          label: "生效中",
          align: "center",
          field: row => row.next_run_time,
          format: val => (val ? "\u2705" : "\u274C"),
          sortable: true
        }
      ],
      visibleColumns: [
        "name",
        "func",
        "trigger",
        "start_date",
        "end_date",
        "next_run_time",
        "pending",
        "activated"
      ],
      currentJob: {},
      isShowDetail: false
    };
  },
  methods: {
    showJobCard(evt, row, index) {
      this.currentJob = row;
      this.isShowCard = true;
    },
    refreshJobs() {
      this.loading = true;
      this.$axios
        .get("/scheduler/jobs")
        .then(res => {
          this.jobs = res.data.data;
          this.loading = false;
        })
        .catch(err => {
          this.loading = false;
          this.$q.notify({
            type: "negative",
            position: "top",
            icon: "warning",
            message: "无法获取产品数据，请确认网络连接是否正常。"
          });
        });
    },
    removeJob() {
      if (this.selected.length === 0) {
        this.$q.notify({
          type: "warning",
          position: "top",
          icon: "warning",
          timeout: 2000,
          message: "请先选择需要删除的任务！"
        });
      } else {
        this.$q
          .dialog({
            title: "确认",
            message: "确认要删除当前选定的任务吗？",
            cancel: true,
            persistent: true,
            focus: "cancel"
          })
          .onOk(() => {
            let id = this.selected[0].id;
            let name = this.selected[0].name;
            this.$axios
              .delete("/scheduler/job/" + id)
              .then(res => {
                this.$q.notify({
                  type: "positive",
                  position: "top",
                  icon: "check_circle",
                  message: "已删除任务：" + name
                });
                this.refreshJobs();
              })
              .catch(err => {
                this.$q.notify({
                  type: "negative",
                  position: "top",
                  icon: "warning",
                  message: "删除任务失败，请确认网络连接是否正常。"
                });
              });
          });
      }
    },
    pauseJob() {
      if (this.selected.length === 0) {
        this.$q.notify({
          type: "warning",
          position: "top",
          icon: "warning",
          timeout: 2000,
          message: "请先选择需要暂停的任务！"
        });
      } else {
        let id = this.selected[0].id;
        let name = this.selected[0].name;
        this.$axios
          .put("/scheduler/job/" + id, {
            action: "pause"
          })
          .then(res => {
            this.$q.notify({
              type: "positive",
              position: "top",
              icon: "check_circle",
              message: "已暂停指定的计划任务：" + name
            });
            this.refreshJobs();
          })
          .catch(err => {
            this.$q.notify({
              type: "negative",
              position: "top",
              icon: "warning",
              message: "暂停任务失败，请确认网络连接是否正常。"
            });
          });
      }
    },
    resumeJob() {
      if (this.selected.length === 0) {
        this.$q.notify({
          type: "warning",
          position: "top",
          icon: "warning",
          timeout: 2000,
          message: "请先选择需要暂停的任务！"
        });
      } else {
        let id = this.selected[0].id;
        let name = this.selected[0].name;
        this.$axios
          .put("/scheduler/job/" + id, {
            action: "resume"
          })
          .then(res => {
            this.$q.notify({
              type: "positive",
              position: "top",
              icon: "check_circle",
              message: "已恢复指定的计划任务：" + name
            });
            this.refreshJobs();
          })
          .catch(err => {
            this.$q.notify({
              type: "negative",
              position: "top",
              icon: "warning",
              message: "恢复运行任务失败，请确认网络连接是否正常。"
            });
          });
      }
    }
  },
  created: function() {
    this.refreshJobs();
  }
};
</script>

<style>
.my-card {
  max-width: 100%;
  min-width: 400px;
}
.text-wrapper {
  white-space: pre-wrap;
}
</style>
