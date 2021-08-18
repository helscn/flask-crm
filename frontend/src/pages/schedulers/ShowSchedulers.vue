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

      <q-tab-panels v-model="tab" animated keep-alive>
        <q-tab-panel name="schedulers" class="q-gutter-md">
          <q-btn-group rounded push>
            <q-btn
              label="新建"
              icon="add_circle_outline"
              @click="$router.push('/schedulers/new')"
              color="primary"
            />
            <q-btn
              label="删除"
              :disable="selected.length !== 1"
              rounded
              icon="delete_forever"
              @click="removeJob"
              color="primary"
            />
            <q-btn
              label="暂停"
              :disable="selected.length !== 1 || !selected[0].next_run_time"
              rounded
              icon="pause"
              @click="pauseJob"
              color="primary"
            />
            <q-btn
              label="激活"
              :disable="selected.length !== 1 || !!selected[0].next_run_time"
              rounded
              icon="play_arrow"
              @click="resumeJob"
              color="primary"
            />
            <q-btn
              label="刷新"
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
          <SchedulerLogs />
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
                :label="currentJob.name"
              />
              <span class="q-ml-md text-subtitle1"> {{ currentJob.func }}</span>
            </div>
          </div>
        </q-card-section>
        <q-separator />
        <q-card-section>
          <div class="text-wrapper">
            <b>开始时间：</b>{{ currentJob.start_date || "无" }}
          </div>
          <div class="text-wrapper">
            <b>结束时间：</b>{{ currentJob.end_date || "无" }}
          </div>
          <div class="text-wrapper">
            <b>下次运行：</b>{{ currentJob.next_run_time || "无" }}
          </div>
          <div class="text-wrapper">
            <b>触发器：</b><br />{{ currentJob.trigger }}
          </div>
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
import SchedulerLogs from "src/components/scheduler/SchedulerLogs.vue";

export default {
  components: { SchedulerLogs },
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
          name: "activated",
          label: "已激活",
          align: "center",
          field: row => row.next_run_time,
          format: val => (val ? "\u2705" : "\u274C"),
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
          align: "left",
          field: row => row.func,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "trigger",
          label: "触发器",
          align: "center",
          field: row => row.trigger.type,
          format: val =>
            val == "date"
              ? "单次任务"
              : val == "interval"
              ? "循环任务"
              : val == "cron"
              ? "定时任务"
              : rval,
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
        }
      ],
      visibleColumns: [
        "activated",
        "name",
        "func",
        "trigger",
        "start_date",
        "end_date",
        "next_run_time"
      ],
      currentJob: {},
      isShowDetail: false
    };
  },
  methods: {
    showJobCard(evt, row, index) {
      this.currentJob = row;
      this.isShowDetail = true;
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
                this.selected = [];
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
            this.selected = [];
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
            this.selected = [];
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
