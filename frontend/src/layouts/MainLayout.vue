<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <TopToolbar />
    </q-header>
    <LeftSideBar />

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import TopToolbar from "components/TopToolbar.vue";
import LeftSideBar from "components/LeftSideBar.vue";

export default {
  name: "MainLayout",
  components: {
    TopToolbar,
    LeftSideBar
  }
};
</script>
