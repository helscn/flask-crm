<template>
  <q-breadcrumbs class="q-px-lg q-py-sm bg-grey-2 shadow-3">
    <q-breadcrumbs-el
      v-for="item in breadList"
      v-bind:key="item.path"
      :label="item.meta.title"
      :icon="item.meta.icon"
      :to="item.path"
    />
  </q-breadcrumbs>
</template>

<script>
export default {
  name: "Breadcrumb",
  data() {
    return {
      breadList: []
    };
  },
  watch: {
    $route() {
      this.getBreadcrumb();
    }
  },
  methods: {
    getBreadcrumb() {
      let matched = this.$route.matched;
      if (matched[0].name === "home") {
        matched[0].path = "/";
      } else {
        matched = [{ path: "/", meta: { title: "首页" } }].concat(matched);
      }

      this.breadList = matched.filter(route => route.meta.title);
    }
  },
  created() {
    this.getBreadcrumb();
  }
};
</script>
