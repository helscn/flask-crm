<template>
  <q-layout view="hHh lpR fFf">
    <q-page-container>
      <div class="q-gutter-y-md" style="fullscreen">
        <q-tabs no-caps class="bg-gray-3  text-primary shadow-2">
          <q-route-tab to="/products/all" exact replace label="所有产品" />
          <q-route-tab
            :to="{ query: { tab: '2' } }"
            exact
            replace
            label="Do nothing"
          />
          <q-route-tab
            :to="{ query: { tab: '3' } }"
            exact
            replace
            label="Navigate to the second tab"
          />
          <q-route-tab
            :to="{ query: { tab: '4' } }"
            exact
            replace
            label="Navigate immediatelly"
          />
        </q-tabs>
      </div>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  data() {
    return {};
  }
};
</script>
