<template>
  <q-page>
    <div class="q-ma-sm row items-start content-start q-gutter-md">
      <ProjectCard v-for="item in projectsList" :key="item.id" v-bind="item" />
    </div>
  </q-page>
</template>

<script>
import ProjectCard from "components/ProjectCard.vue";
export default {
  components: { ProjectCard },
  data() {
    return {
      projectsList: [
        {
          id: 1,
          name: "测试项目",
          description: "这是项目描述，说明项目的背景及制作要求。",
          creater: "何罗生",
          created_date: "2021/23/23 08:21:22",
          path: "/table"
        },
        {
          id: 2,
          name: "测试项目",
          description: "这是项目描述，说明项目的背景及制作要求。",
          creater: "何罗生",
          created_date: "2021/23/23 08:21:22",
          path: "/table"
        },
        {
          id: 3,
          name: "Can you Mary me, my beautiful princess",
          description:
            "这是一个测试，用于展示显示测试内容震左吉大南校大方地说安抚加大开发地地载需要在地革震奈斯。",
          creater: "何罗生",
          created_date: "2021/23/23 08:21:22",
          path: "/table"
        },
        {
          id: 4,
          name: "Can you Mary me, my beautiful princess",
          description:
            "这是一个测试，用于展示显示测试内容震左吉大南校大方地说安抚加大开发地地载需要在地革震奈斯。这是一个测试，用于展示显示测试内容震左吉大南校大方地说安抚加大开发地地载需要在地革震奈斯。这是一个测试，用于展示显示测试内容震左吉大南校大方地说安抚加大开发地地载需要在地革震奈斯。",
          creater: "何罗生",
          created_date: "2021/23/23 08:21:22",
          path: "/table"
        },
        {
          id: 5,
          name: "Can you Mary me, my beautiful princess",
          description:
            "这是一个测试，用于展示显示测试内容震左吉大南校大方地说安抚加大开发地地载需要在地革震奈斯。",
          creater: "何罗生",
          created_date: "2021/23/23 08:21:22",
          path: "/table"
        }
      ]
    };
  }
};
</script>

<style scoped>
.my-card {
  width: 350px;
}
</style>
