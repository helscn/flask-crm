<template>
  <q-drawer
    show-if-above
    v-model="isShowLeft"
    side="left"
    :width="250"
    elevated
  >
    <q-item clickable v-ripple>
      <q-item-section top avatar>
        <q-avatar rounded size="48px">
          <img src="images/Avatar.png" />
        </q-avatar>
      </q-item-section>
      <q-item-section>
        <q-item-label>{{ name }}</q-item-label>
        <q-item-label caption>{{ role_name }}</q-item-label>
      </q-item-section>
    </q-item>
    <q-separator spaced inset />

    <PageListItem v-for="item in projectsList" :key="item.name" v-bind="item" />
  </q-drawer>
</template>

<script>
import { mapState } from "vuex";
import PageListItem from "components/PageListItem.vue";

export default {
  name: "LeftSideBar",
  components: { PageListItem },
  data() {
    return {
      projectsList: [
        {
          name: "客户管理",
          icon: "people",
          path: "/customers"
        },
        {
          name: "产品管理",
          icon: "business_center",
          path: "/products/all"
        },
        {
          name: "供应商管理",
          icon: "support_agent",
          path: "/suppliers"
        },
        {
          name: "客户询价",
          icon: "request_quote",
          path: "/quotations"
        },
        {
          name: "订单管理",
          icon: "paid",
          path: "/orders"
        },
        {
          name: "数据统计",
          icon: "leaderboard",
          path: "/stat"
        },
        {
          name: "用户管理",
          icon: "manage_accounts",
          path: "/users"
        },
        {
          name: "文件上传",
          icon: "cloud_upload",
          path: "/upload"
        }
      ]
    };
  },
  methods: {},
  computed: {
    ...mapState({
      name: state => state.auth.nickname,
      role_name: state => state.auth.role_name
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
    this.$store.dispatch("auth/refreshLogin");
  }
};
</script>
