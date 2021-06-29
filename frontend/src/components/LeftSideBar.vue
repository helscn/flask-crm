<template>
  <q-drawer
    show-if-above
    v-model="isShowLeft"
    side="left"
    :width="250"
    elevated
  >
    <q-item clickable v-ripple @click="showIndex">
      <q-item-section top avatar>
        <q-avatar rounded size="48px">
          <img src="/images/Avatar.png" />
        </q-avatar>
      </q-item-section>
      <q-item-section>
        <q-item-label>{{ name }}</q-item-label>
        <q-item-label caption>{{ title }}</q-item-label>
        <q-item-label caption>{{ department }}</q-item-label>
      </q-item-section>
    </q-item>
    <q-separator spaced inset />

    <ProjectItem v-for="item in projectsList" :key="item.name" v-bind="item" />
  </q-drawer>
</template>

<script>
import { mapState } from "vuex";
import ProjectItem from "components/ProjectItem.vue";

export default {
  name: "LeftSideBar",
  components: { ProjectItem },
  data() {
    return {
      projectsList: [
        {
          name: "测试项目",
          description: "这是项目描述，说明项目的背景及制作要求。",
          path: "/projects"
        },
        {
          name: "Can you Mary me, my beautiful princess",
          description:
            "这是一个测试，用于展示显示测试内容震左吉大南校大方地说安抚加大开发地地载需要在地革震奈斯。",
          path: "/table"
        },
        {
          name: "文件上传",
          description: "这是一个测试，用于展示文件上传组件。",
          path: "/upload"
        }
      ]
    };
  },
  methods: {
    showIndex: function() {
      this.$router.push("/");
    }
  },
  computed: {
    ...mapState({
      name: state => state.auth.name,
      title: state => state.auth.title,
      department: state => state.auth.department,
      phone: state => state.auth.phone,
      email: state => state.auth.email
    }),
    isShowLeft: {
      get: function() {
        return this.$store.state.isShowLeft;
      },
      set: function(value) {
        this.$store.commit("setLeftSideBar", value);
      }
    }
  },

  mounted: function() {
    if (
      this.$store.state.auth.name == "" &&
      this.$store.state.auth.token != ""
    ) {
      this.$store.dispatch("auth/refreshLogin", this);
    }
  }
};
</script>
