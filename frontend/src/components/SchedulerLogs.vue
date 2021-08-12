<template>
  <div>
    <div class="q-gutter-md q-mb-md">
      <q-btn
        label="刷新日志"
        rounded
        icon="refresh"
        @click="refreshLogs"
        color="primary"
      />
      <q-btn
        label="清除当前日志"
        :disable="pagination.rowsNumber == 0"
        rounded
        icon="delete_forever"
        @click="clearLogs"
        color="primary"
      />
    </div>
    <q-table
      ref="scheduler_logs"
      dense
      :loading="loading"
      :data="data"
      :columns="columns"
      row-key="id"
      :pagination.sync="pagination"
      :filter="filter"
      :visible-columns="visibleColumns"
      @row-dblclick="showLogDetail"
      @request="onRequest"
      table-header-class="bg-grey-2"
    >
      <template v-slot:top>
        <q-input
          color="black"
          dense
          debounce="500"
          v-model="filter"
          placeholder="搜索任务日志"
        >
          <template v-slot:prepend>
            <q-icon name="search" />
          </template>
          <template v-if="filter" v-slot:append>
            <q-icon name="close" @click="filter = ''" class="cursor-pointer" />
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

    <q-dialog v-model="isShowDetail">
      <q-card class="my-card">
        <q-card-section>
          <div class="row no-wrap items-center">
            <div class="col">
              <q-badge
                class="text-subtitle2"
                color="accent"
                align="middle"
                :label="currentLog.type"
              />
              <span class="text-subtitle1 q-ml-md">{{ currentLog.func }}</span>
              <span class="q-ml-md text-subtitle2 text-grey">
                @ {{ currentLog.date }}</span
              >
            </div>
          </div>
        </q-card-section>
        <q-separator />
        <q-card-section>
          <div class="text-wrapper">{{ currentLog.message }}</div>
          <br />
          <div class="text-wrapper">{{ currentLog.detail }}</div>
        </q-card-section>

        <q-separator />

        <q-card-actions align="right">
          <q-btn v-close-popup flat color="primary" label="关闭" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: "SchedulerLogs",
  data() {
    return {
      loading: false,
      data: [],
      filter: "",
      selected: [],
      pagination: {
        sortBy: "date",
        descending: true,
        page: 1,
        rowsPerPage: 10,
        rowsNumber: 0
      },
      columns: [
        {
          name: "id",
          label: "ID",
          align: "center",
          field: row => row.id,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "date",
          label: "时间",
          align: "center",
          field: row => row.date,
          format: val => val || "(无)",
          sortable: true
        },
        {
          name: "type",
          label: "类别",
          align: "left",
          field: row => row.type,
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
          field: row => row.trigger,
          format: val =>
            val == "date"
              ? "单次任务"
              : val == "interval"
              ? "循环任务"
              : val == "cron"
              ? "定时任务"
              : val,
          sortable: true
        },
        {
          name: "run_time",
          label: "计划执行时间",
          align: "center",
          field: row => row.run_time,
          format: val => val || "(无)",
          sortable: true
        },
        {
          name: "message",
          label: "日志内容",
          align: "left",
          field: row => row.message,
          format: val => val || "(无)",
          sortable: true
        },
        {
          name: "detail",
          label: "日志详情",
          align: "left",
          field: row => row.detail,
          format: val => val || "(无)",
          sortable: true
        }
      ],
      visibleColumns: [
        "date",
        "type",
        "name",
        "func",
        "trigger",
        "run_time",
        "message"
      ],
      currentLog: {},
      isShowDetail: false
    };
  },

  methods: {
    showLogDetail(evt, row, index) {
      this.currentLog = row;
      this.isShowDetail = true;
    },

    onRequest(props) {
      const { page, rowsPerPage, sortBy, descending } = props.pagination;
      const filter = props.filter;
      this.loading = true;
      this.$axios
        .get("/scheduler/logs", {
          params: {
            page: page,
            per_page: rowsPerPage,
            sort_by: sortBy,
            descending: descending,
            filter: filter
          }
        })
        .then(res => {
          this.data = res.data.data;
          this.pagination.page = res.data.page;
          this.pagination.rowsPerPage = res.data.per_page;
          this.pagination.sortBy = res.data.sort_by;
          this.pagination.descending = res.data.descending;
          this.pagination.rowsNumber = res.data.total;
          this.loading = false;
        })
        .catch(err => {
          this.$q.notify({
            type: "negative",
            position: "top",
            icon: "error",
            message: "无法获取日志记录，请确认网络连接是否正常！",
            timeout: 1000
          });
          this.loading = false;
        });
    },

    clearLogs() {
      this.loading = true;
      this.$axios
        .delete("/scheduler/logs", {
          params: {
            filter: this.filter
          }
        })
        .then(res => {
          this.$q.notify({
            type: "positive",
            position: "top",
            icon: "check_circle",
            message: "已清除当前日志记录。"
          });
          this.data = [];
          this.pagination.rowsNumber = 0;
          this.loading = false;
        })
        .catch(err => {
          this.$q.notify({
            type: "negative",
            position: "top",
            icon: "error",
            message: "无法清除当前日志记录，请确认网络连接是否正常！",
            timeout: 1000
          });
          this.loading = false;
        });
    },

    refreshLogs() {
      this.onRequest({
        pagination: this.pagination,
        filter: this.filter
      });
    }
  },

  created: function() {
    this.refreshLogs();
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
