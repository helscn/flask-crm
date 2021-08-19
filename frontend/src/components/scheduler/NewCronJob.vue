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
            定时任务的计划开始时间。
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
            定时任务的计划结束时间，如果不输入则无限期执行。
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
      <q-input dense v-model="year" label="年" class="col q-mr-md">
        <q-tooltip :delay="400">
          年份，取值为4位数字的年份，或使用表达式。
        </q-tooltip>
      </q-input>
      <q-input dense v-model="month" label="月" class="col q-ml-md">
        <q-tooltip :delay="400">
          月份，取值1-12，或使用表达式。
        </q-tooltip>
      </q-input>
    </div>
    <div class="row justify-between">
      <q-input dense v-model="day" label="日" class="col q-mr-md">
        <q-tooltip :delay="400">
          每月的第几日，取值1-31，或使用表达式。
        </q-tooltip>
      </q-input>
      <q-input dense v-model="week" label="周" class="col q-ml-md">
        <q-tooltip :delay="400">
          每年的周数，取值1-53，或使用表达式。
        </q-tooltip>
      </q-input>
    </div>
    <div class="row justify-between">
      <q-input dense v-model="day_of_wek" label="星期" class="col q-mr-md">
        <q-tooltip :delay="400">
          每周的第几天或者星期几 (范围0-6 或者 mon,tue,wed,thu,fri,sat,sun)
        </q-tooltip>
      </q-input>
      <q-input dense v-model="hour" label="小时" class="col q-ml-md">
        <q-tooltip :delay="400">
          每天的小时数，取值0-23，或使用表达式。
        </q-tooltip>
      </q-input>
    </div>
    <div class="row justify-between">
      <q-input dense v-model="minute" label="分钟" class="col q-mr-md">
        <q-tooltip :delay="400">
          每小时的分钟数，取值0-59，或使用表达式。
        </q-tooltip>
      </q-input>
      <q-input dense v-model="second" label="秒" class="col q-ml-md">
        <q-tooltip :delay="400">
          每分钟的秒数，取值0-59，或使用表达式。
        </q-tooltip>
      </q-input>
    </div>

    <div class="row justify-around q-py-md">
      <q-btn
        flat
        color="primary"
        label="表达式说明"
        :icon="expanded ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
        @click="expanded = !expanded"
      />
      <q-btn color="primary" icon="save" label="保存" @click="save" />
      <q-btn color="primary" icon="cancel" label="取消" @click="cancel" />
    </div>
    <q-slide-transition>
      <div v-show="expanded" class="q-mb-md">
        <q-separator />
        <q-markup-table>
          <thead>
            <tr>
              <th class="text-left">表达式</th>
              <th class="text-left">适用字段</th>
              <th class="text-left">任务执行说明</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th class="text-left">*</th>
              <th class="text-left">所有字段</th>
              <th class="text-left">每个值都执行</th>
            </tr>
            <tr>
              <th class="text-left">*/a</th>
              <th class="text-left">所有字段</th>
              <th class="text-left">每隔a间隔执行，从最小值a开始</th>
            </tr>
            <tr>
              <th class="text-left">a-b</th>
              <th class="text-left">所有字段</th>
              <th class="text-left">取值范围为a-b时执行</th>
            </tr>
            <tr>
              <th class="text-left">a-b/c</th>
              <th class="text-left">所有字段</th>
              <th class="text-left">在a-b范围内每隔c间隔执行</th>
            </tr>
            <tr>
              <th class="text-left">xth y</th>
              <th class="text-left">天数字段</th>
              <th class="text-left">每月第x个星期y执行</th>
            </tr>
            <tr>
              <th class="text-left">last x</th>
              <th class="text-left">天数字段</th>
              <th class="text-left">每月最后一个星期x执行</th>
            </tr>
            <tr>
              <th class="text-left">last</th>
              <th class="text-left">天数字段</th>
              <th class="text-left">每月的最后一天执行</th>
            </tr>
            <tr>
              <th class="text-left">x,y,z</th>
              <th class="text-left">所有字段</th>
              <th class="text-left">
                逗号分隔匹配多个表达式，表达式可以为数字或以上任意表达式
              </th>
            </tr>
          </tbody>
        </q-markup-table>
      </div>
    </q-slide-transition>
  </div>
</template>

<script>
export default {
  name: "NewCronJob",
  data() {
    return {
      name: null,
      func: null,
      start_date: null,
      end_date: null,
      year: null,
      month: null,
      day: null,
      week: null,
      day_of_wek: null,
      hour: null,
      minute: null,
      second: null,
      expanded: false
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
          trigger: "cron",
          fields: {}
        };
        if (this.start_date) {
          data.start_date = this.start_date;
        }
        if (this.end_date) {
          data.end_date = this.end_date;
        }
        if (this.year) {
          data.fields.year = this.year;
        }
        if (this.month) {
          data.fields.month = this.month;
        }
        if (this.day) {
          data.fields.day = this.day;
        }
        if (this.week) {
          data.fields.week = this.week;
        }
        if (this.day_of_week) {
          data.fields.day = this.day_of_week;
        }
        if (this.hour) {
          data.fields.hour = this.hour;
        }
        if (this.minute) {
          data.fields.minute = this.minute;
        }
        if (this.second) {
          data.fields.second = this.second;
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
        !(
          this.year ||
          this.month ||
          this.day ||
          this.week ||
          this.day_of_week ||
          this.hour ||
          this.minute ||
          this.second
        )
      ) {
        this.$q.notify({
          type: "warning",
          position: "center",
          icon: "warning",
          message: "创建定时执行的计划任务至少需要输入一个时间字段。",
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
