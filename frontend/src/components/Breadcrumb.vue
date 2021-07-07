<template>
  <q-breadcrumbs
    gutter="sm"
    class="q-px-lg q-py-sm bg-grey-2 shadow-3 text-subtitle1"
  >
    <template v-slot:separator>
      <q-icon size="1.2em" name="arrow_forward" />
    </template>
    <q-breadcrumbs-el
      v-for="item in breadList"
      v-bind:key="item.path"
      :label="item.title"
      :icon="item.icon"
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
      let breadcrumbs = [];
      matched.forEach((v, i) => {
        if (v.meta && (v.meta.title || v.meta.icon)) {
          breadcrumbs.push({
            path: v.path || "/",
            title: v.meta.title || undefined,
            icon: v.meta.icon || undefined
          });
        }
      });
      this.breadList = breadcrumbs;
    }
  },
  created() {
    this.getBreadcrumb();
  }
};
</script>
