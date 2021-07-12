<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <TopToolbar />
    </q-header>
    <LeftSideBar />
    <q-page-container>
      <breadcrumb />
      <keep-alive>
        <router-view v-if="$route.meta.keepAlive">
          <!-- 这里是会被缓存的视图组件，比如 Home！ -->
        </router-view>
      </keep-alive>

      <router-view v-if="!$route.meta.keepAlive">
        <!-- 这里是不被缓存的视图组件，比如 Edit！ -->
      </router-view>
    </q-page-container>
  </q-layout>
</template>

<script>
import TopToolbar from "components/TopToolbar.vue";
import LeftSideBar from "components/LeftSideBar.vue";
import Breadcrumb from "components/Breadcrumb.vue";

export default {
  name: "MainLayout",
  components: {
    TopToolbar,
    LeftSideBar,
    Breadcrumb
  },
  created: function() {
    if (!this.$cookies.isKey("Token")) {
      this.$router.push("/login");
    }
    this.$store
      .dispatch("auth/refreshLogin")
      .then(res => {
        this.$store.dispatch("products/fetchProducts").catch(err => {
          this.$q.notify({
            type: "negative",
            position: "top",
            icon: "warning",
            message: "无法获取产品数据，请确认网络连接是否正常。"
          });
        });
      })
      .catch(err => {
        this.$q.notify({
          type: "negative",
          position: "top",
          icon: "error",
          message: "当前用户未认证，请重新登录..."
        });
        setTimeout(() => {
          this.$router.push("/login");
        }, 1500);
      });
  }
};
</script>
