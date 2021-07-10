<template>
  <q-item :to="path" clickable v-ripple>
    <q-item-section avatar>
      <q-avatar rounded :icon="icon"> </q-avatar>
    </q-item-section>
    <q-item-section>
      <q-item-label :lines="1">{{ name }}</q-item-label>
    </q-item-section>
  </q-item>
</template>

<script>
export default {
  name: "MenuListItem",
  props: {
    path: {
      type: String,
      default: ""
    },

    name: {
      type: String,
      default: ""
    },

    description: {
      type: String,
      default: ""
    },

    icon: {
      type: String,
      default: "description"
    }
  }
};
</script>
