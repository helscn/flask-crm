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
        <q-tab name="date" label="单次任务" icon="event" />
        <q-tab name="interval" label="循环任务" icon="loop" />
        <q-tab name="cron" label="定时任务" icon="schedule" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="tab" animated keep-alive>
        <q-tab-panel name="date" class="q-py-lg row justify-center">
          <NewDataJob @save="save" @cancel="cancel" />
        </q-tab-panel>
        <q-tab-panel name="interval" class="q-py-lg row justify-center">
          <NewIntervalJob @save="save" @cancel="cancel" />
        </q-tab-panel>
        <q-tab-panel name="cron" class="q-py-lg row justify-center">
          <NewCronJob @save="save" @cancel="cancel" />
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
  </q-page>
</template>

<script>
import NewDataJob from "components/scheduler/NewDateJob.vue";
import NewIntervalJob from "components/scheduler/NewIntervalJob.vue";
import NewCronJob from "components/scheduler/NewCronJob.vue";

export default {
  name: "NewScheduler",
  components: { NewDataJob, NewIntervalJob, NewCronJob },
  data() {
    return {
      tab: "date",
      date: null
    };
  },
  methods: {
    cancel() {
      this.$router.go(-1);
    },
    save(data) {
      this.$axios
        .post("/scheduler/jobs", data)
        .then(res => {
          this.$q.notify({
            type: "positive",
            position: "top",
            icon: "check_circle",
            message: "计划任务创建成功。",
            timeout: 1000
          });
          this.$router.push("/schedulers");
        })
        .catch(error => {
          this.$q.notify({
            type: "negative",
            position: "top",
            icon: "error",
            message: "创建计划任务出错，请检查网络连接是否正常。",
            timeout: 1000
          });
        });
    }
  }
};
</script>
