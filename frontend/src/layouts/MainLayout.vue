<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <TopToolbar />
    </q-header>
    <LeftSideBar />
    <q-page-container>
      <breadcrumb />
      <router-view />
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
  }
};
</script>
