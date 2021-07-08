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
  },
  created: function() {
    if (!this.$cookies.isKey("Token")) {
      this.$router.push("/login");
    }
    this.$store
      .dispatch("auth/refreshLogin")
      .then(res => {
        this.$store.dispatch("products/fetchProducts");
      })
      .catch(err => {
        this.$q.notify({
          type: "negative",
          position: "center",
          icon: "announcement",
          message: "当前用户未认证，请重新登录...",
          timeout: 500,
          progress: true
        });
        setTimeout(() => {
          this.$router.push("/login");
        }, 1500);
      });
  }
};
</script>
