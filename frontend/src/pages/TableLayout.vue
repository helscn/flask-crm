<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <div class="flex flex-center container">
        <table class="centerContent" cellspacing="0" border="0">
          <thead>
            <tr>
              <th>Title</th>
              <th>Caption</th>
              <th>
                <div>
                  Icon<img
                    @click="showInfo"
                    src="~assets/quasar-logo-vertical.svg"
                  />
                </div>
              </th>
              <th>Link</th>
            </tr>
          </thead>
          <tbody>
            <tr border="1" v-for="link in links" :key="link">
              <td width="5%">{{ link.title }}</td>
              <td width="30%">{{ link.caption }}</td>
              <td width="20%"><img :src="link.icon" /></td>
              <td width="30%">{{ link.link }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
const linksData = [
  {
    title: "Docs",
    caption: "quasar.dev",
    icon: "@/ Helscnassets/a.jpg",
    link: "https://quasar.dev"
  },
  {
    title: "Github",
    caption: "github.com/quasarframework",
    icon: "~assets/b.jpg",
    link: "https://github.com/quasarframework"
  },
  {
    title: "Discord Chat Channel",
    caption: "chat.quasar.dev",
    icon: "~assets/c.jpg",
    link: "https://chat.quasar.dev"
  }
];

export default {
  name: "TableLayout",
  methods: {
    showInfo: function(event) {
      console.debug(this.$q);
      this.$axios
        .get("/hello")
        .then(response => {
          this.$q.notify({
            // 必需的参数是消息：
            message: response.data,

            /*
             * 以下所有参数都是可选的：
             */

            timeout: 1000, // 以毫秒为单位; 0意味着没有超时

            // "type"添加一个颜色和图标，
            // 所以你不需要指定它们。
            // 可用的值: 'positive', 'negative', 'warning', 'info'
            type: "negative",

            //color: "info",
            //textColor: "black", // 如果默认的“white”不适合

            icon: "wifi",
            detail: "Optional detail message.",
            position: "top-right", // 'top', 'left', 'bottom-left'等

            actions: [
              {
                label: "OK",
                icon: "timer", // 可选
                handler: () => {
                  console.log("acting");
                }
              },
              {
                label: "Cancel",
                handler: () => {
                  console.log("dismissed");
                }
              }
            ]
          });
        })
        .catch(() => {
          this.$q.notify({
            color: "negative",
            position: "top",
            message: "Loading failed",
            icon: "report_problem"
          });
        });
    }
  },
  data() {
    return {
      leftDrawerOpen: false,
      links: linksData
    };
  }
};
</script>

<style scoped>
.centerContent {
  width: 1000px;
  text-align: center;
}

.container {
  margin: 20px;
}

tr {
  height: 100px;
  padding: 20px;
}
</style>
