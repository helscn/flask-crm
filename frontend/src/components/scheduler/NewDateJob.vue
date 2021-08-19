<template>
  <div
    class="col-xs-12 col-sm-8 col-md-5 col-xl-3 shadow-2 q-ma-xs q-pr-md q-gutter-md"
  >
    <q-input
      dense
      v-model.trim="name"
      label="任务名称*"
      :rules="[val => !!val || '必须输入任务名称']"
    >
      <q-tooltip :delay="400" anchor="top middle">
        请输入新任务的名称，如果与已存在的任务名称相同则会覆盖旧的计划任务。
      </q-tooltip>
    </q-input>
    <q-input
      dense
      v-model.trim="func"
      label="任务模块*"
      :rules="[val => !!val || '必须输入要运行的任务模块']"
    >
      <q-tooltip :delay="400" anchor="top middle">
        需要运行的计划任务引用，任务模块必须放在服务器 jobs 文件夹中
        <div>格式: <i>模块名:入口函数名</i></div>
      </q-tooltip>
    </q-input>
    <div>
      <div class="text-grey-7 text-subtitle3">运行日期：</div>
      <q-input dense filled v-model="run_date" mask="####-##-## ##:##:##">
        <q-tooltip :delay="400" anchor="top middle">
          任务的计划运行时间，如果不输入则立即运行。
        </q-tooltip>
        <template v-slot:prepend>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy transition-show="scale" transition-hide="scale">
              <q-date v-model="run_date" mask="YYYY-MM-DD HH:mm:ss">
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
              <q-time v-model="run_date" mask="YYYY-MM-DD HH:mm:ss" format24h>
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-time>
            </q-popup-proxy>
          </q-icon>
        </template>
      </q-input>
    </div>
    <div class="row justify-around q-py-md">
      <q-btn color="primary" icon="save" label="保存" @click="save" />
      <q-btn color="primary" icon="cancel" label="取消" @click="cancel" />
    </div>
  </div>
</template>

<script>
export default {
  name: "NewDateJob",
  data() {
    return {
      run_date: null,
      name: null,
      func: null
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
          trigger: "date",
          fields: {}
        };
        if (this.run_date) {
          data.fields.run_date = this.run_date;
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
      } else {
        return true;
      }
    }
  }
};
</script>
