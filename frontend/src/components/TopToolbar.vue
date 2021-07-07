<template>
  <q-toolbar class="bg-primary glossy text-white">
    <q-btn dense flat round icon="menu" @click="toggleLeftSideBar" />
    <q-toolbar-title>
      <span>
        <q-avatar>
          <img src="/icons/SYE.ico" />
        </q-avatar>
        {{ title }}
      </span>
    </q-toolbar-title>

    <q-btn
      class="glossy"
      round
      color="deep-orange"
      icon="logout"
      size="sm"
      @click.stop="logout"
    >
      <q-tooltip>退出</q-tooltip>
    </q-btn>
  </q-toolbar>
</template>

<script>
export default {
  name: "TopToolbar",
  data() {
    return {
      title: "CRM管理系统"
    };
  },
  methods: {
    toggleLeftSideBar: function() {
      this.$store.commit("toggleLeftSideBar");
    },
    logout: function() {
      let _this = this;
      _this.$store.commit("auth/logout");
      _this.$q.notify({
        type: "warning",
        position: "center",
        icon: "announcement",
        message: "已登出，正在跳转至登录界面...",
        timeout: 500,
        progress: true
      });
      setTimeout(() => {
        _this.$router.push("/login");
      }, 1000);
    }
  }
};
</script>
