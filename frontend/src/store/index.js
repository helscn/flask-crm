import Vue from "vue";
import Vuex from "vuex";

// import example from './module-example'
import auth from "./auth";
import products from "./products";

Vue.use(Vuex);

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function(/* { ssrContext } */) {
  const Store = new Vuex.Store({
    state() {
      return {
        isShowLeft: true,
        leftMenuList: [
          {
            name: "客户管理",
            icon: "people",
            path: "/customers"
          },
          {
            name: "产品管理",
            icon: "business_center",
            path: "/products"
          },
          { name: "供应商管理", icon: "support_agent", path: "/suppliers" },
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
            path: "/stats"
          },
          {
            name: "设置",
            icon: "settings",
            path: "/settings"
          },
          {
            name: "用户管理",
            icon: "manage_accounts",
            path: "/users"
          }
        ]
      };
    },
    mutations: {
      toggleLeftSideBar(state) {
        state.isShowLeft = !state.isShowLeft;
      },
      setLeftSideBar(state, isShow) {
        state.isShowLeft = !!isShow;
      }
    },

    modules: {
      auth,
      products
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEBUGGING
  });

  return Store;
}
