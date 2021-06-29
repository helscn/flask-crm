<template>
  <q-card class="my-card q-my-sm q-ml-lg" bordered>
    <q-card-section horizontal>
      <q-item :to="path" clickable v-ripple>
        <q-item-section avatar>
          <q-avatar>
            <img :src="icon" />
          </q-avatar>
        </q-item-section>

        <q-item-section>
          <q-item-label>{{ name }}</q-item-label>
          <q-item-label caption>
            {{ creater }} @ {{ created_date }}
          </q-item-label>
        </q-item-section>
      </q-item>
    </q-card-section>
    <q-card-section class="q-py-sm  ">
      <q-item-label>
        {{ description }}
      </q-item-label>
    </q-card-section>

    <q-separator />

    <q-card-actions class="justify-end q-py-none">
      <q-btn flat round color="primary" icon="group_add"
        ><q-tooltip>增加项目组成员</q-tooltip></q-btn
      >
      <q-btn flat round color="accent" icon="group_remove"
        ><q-tooltip>删除项目组成员</q-tooltip></q-btn
      >
      <q-btn flat round color="red" icon="favorite"
        ><q-tooltip>退出项目组</q-tooltip></q-btn
      >
      <q-btn flat round color="grey" icon="favorite"
        ><q-tooltip>加入项目组</q-tooltip></q-btn
      >
    </q-card-actions>
  </q-card>
</template>

<script>
export default {
  name: "ProjectCard",
  props: {
    path: {
      type: String,
      default: ""
    },

    id: {
      type: Number
    },

    name: {
      type: String,
      default: ""
    },

    creater: {
      type: String,
      default: ""
    },

    created_date: {
      type: String,
      default: ""
    },

    description: {
      type: String,
      default: ""
    },
    icon: {
      type: String,
      default: "/images/Avatar.png"
    }
  }
};
</script>

<style scoped></style>
