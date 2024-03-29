<template>
  <div
    class="col-xs-12 col-sm-10 col-md-6 col-xl-4 shadow-2 q-ma-xs q-pr-md q-gutter-md"
  >
    <div class="row justify-between">
      <q-input
        dense
        v-model.trim="name"
        label="任务名称*"
        :rules="[val => !!val || '必须输入任务名称']"
        class="col q-mr-md"
      >
        <q-tooltip :delay="400">
          请输入新任务的名称，如果与已存在的任务名称相同则会覆盖旧的计划任务。
        </q-tooltip>
      </q-input>
      <q-input
        dense
        v-model.trim="func"
        label="任务模块*"
        :rules="[val => !!val || '必须输入要运行的任务模块']"
        class="col q-ml-md"
      >
        <q-tooltip :delay="400">
          需要运行的计划任务引用，任务模块必须放在服务器 jobs 文件夹中
          <div>格式: <i>模块名:入口函数名</i></div>
        </q-tooltip>
      </q-input>
    </div>
    <div class="row">
      <div class="col q-mr-md">
        <div class="text-grey-7 text-subtitle3">开始时间：</div>
        <q-input
          dense
          filled
          v-model="start_date"
          mask="####-##-## ##:##:##"
          class="col"
        >
          <q-tooltip :delay="400">
            循环任务的计划开始时间。
          </q-tooltip>
          <template v-slot:prepend>
            <q-icon name="event" class="cursor-pointer">
              <q-popup-proxy transition-show="scale" transition-hide="scale">
                <q-date v-model="start_date" mask="YYYY-MM-DD HH:mm:ss">
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-date>
              </q-popup-proxy>
            </q-icon>
          </template>

          <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
              <q-popup-proxy transition-show="scale" transition-hide="scale">
                <q-time
                  v-model="start_date"
                  mask="YYYY-MM-DD HH:mm:ss"
                  format24h
                >
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-time>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
      </div>
      <div class="col q-ml-md">
        <div class="text-grey-7 text-subtitle3">结束时间：</div>
        <q-input
          dense
          filled
          v-model="end_date"
          mask="####-##-## ##:##:##"
          class="col"
        >
          <q-tooltip :delay="400">
            循环任务的计划结束时间，如果不输入则无限期执行。
          </q-tooltip>
          <template v-slot:prepend>
            <q-icon name="event" class="cursor-pointer">
              <q-popup-proxy transition-show="scale" transition-hide="scale">
                <q-date v-model="end_date" mask="YYYY-MM-DD HH:mm:ss">
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-date>
              </q-popup-proxy>
            </q-icon>
          </template>

          <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
              <q-popup-proxy transition-show="scale" transition-hide="scale">
                <q-time v-model="end_date" mask="YYYY-MM-DD HH:mm:ss" format24h>
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-time>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
      </div>
    </div>
    <div class="row justify-between">
      <q-input
        dense
        v-model.number="weeks"
        type="number"
        label="星期数"
        class="col q-mr-md"
      >
        <q-tooltip :delay="400">
          计划任务每次运行的间隔星期数。
        </q-tooltip>
      </q-input>
      <q-input
        dense
        v-model.number="days"
        type="number"
        label="天数"
        class="col q-ml-md"
      >
        <q-tooltip :delay="400">
          计划任务每次运行的间隔天数。
        </q-tooltip>
      </q-input>
    </div>
    <div class="row justify-between">
      <q-input
        dense
        v-model.number="hours"
        type="number"
        label="小时数"
        class="col q-mr-md"
      >
        <q-tooltip :delay="400">
          计划任务每次运行的间隔小时数。
        </q-tooltip>
      </q-input>
      <q-input
        dense
        v-model.number="minutes"
        type="number"
        label="分钟数"
        class="col q-ml-md"
      >
        <q-tooltip :delay="400">
          计划任务每次运行的间隔分钟数。
        </q-tooltip>
      </q-input>
    </div>
    <div class="row justify-between">
      <q-input
        dense
        v-model.number="seconds"
        type="number"
        label="秒数"
        class="col q-mr-md"
      >
        <q-tooltip :delay="400">
          计划任务每次运行的间隔秒数。
        </q-tooltip>
      </q-input>
      <div class="col"></div>
    </div>
    <div class="row justify-around q-py-md">
      <q-btn color="primary" icon="save" label="保存" @click="save" />
      <q-btn color="primary" icon="cancel" label="取消" @click="cancel" />
    </div>
  </div>
</template>

<script>
export default {
  name: "NewIntervalJob",
  data() {
    return {
      name: null,
      func: null,
      start_date: null,
      end_date: null,
      weeks: null,
      days: null,
      hours: null,
      minutes: null,
      seconds: null
    };
  },
  methods: {
    cancel() {
      this.$emit("cancel");
    },
    save: function() {
      if (this.inputIsOk) {
        const data = {
          name: this.name,
          func: this.func,
          trigger: "interval",
          fields: {}
        };
        if (this.start_date) {
          data.start_date = this.start_date;
        }
        if (this.end_date) {
          data.end_date = this.end_date;
        }
        if (this.weeks) {
          data.fields.weeks = this.weeks;
        }
        if (this.days) {
          data.fields.days = this.days;
        }
        if (this.hours) {
          data.fields.hours = this.hours;
        }
        if (this.minutes) {
          data.fields.minutes = this.minutes;
        }
        if (this.seconds) {
          data.fields.seconds = this.seconds;
        }
        this.$emit("save", data);
      }
    }
  },
  computed: {
    inputIsOk: function() {
      if (!this.name || !this.func) {
        this.$q.notify({
          type: "warning",
          position: "center",
          icon: "warning",
          message: "请输入计划任务名称及需要运行的任务模块！",
          timeout: 1000
        });
        return false;
      } else if (this.start_date && this.end_date <= this.start_date) {
        this.$q.notify({
          type: "warning",
          position: "center",
          icon: "warning",
          message: "计划任务结束时间必须大于开始时间。",
          timeout: 1000
        });
        return false;
      } else if (
        !(this.weeks || this.days || this.hours || this.minutes || this.seconds)
      ) {
        this.$q.notify({
          type: "warning",
          position: "center",
          icon: "warning",
          message: "创建循环执行的计划任务至少需要输入一个时间间隔。",
          timeout: 1000
        });
        return false;
      } else {
        return true;
      }
    }
  }
};
</script>
