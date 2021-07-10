<template>
  <q-toolbar class="bg-primary glossy text-white">
    <q-btn dense flat round icon="menu" @click="toggleLeftSideBar" />
    <q-toolbar-title>
      {{ title }}
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
      title: "产品客户管理系统"
    };
  },
  methods: {
    toggleLeftSideBar: function() {
      this.$store.commit("toggleLeftSideBar");
    },
    logout: function() {
      this.$store.commit("auth/logout");
      this.$q.notify({
        type: "warning",
        position: "center",
        icon: "announcement",
        message: "已登出，正在跳转至登录界面...",
        timeout: 500,
        progress: true
      });
      setTimeout(() => {
        this.$router.push("/login");
      }, 1500);
    }
  }
};
</script>
