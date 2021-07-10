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

    <MenuListItem v-for="item in menuList" :key="item.name" v-bind="item" />
  </q-drawer>
</template>

<script>
import { mapState } from "vuex";
import MenuListItem from "src/components/MenuListItem.vue";

export default {
  name: "LeftSideBar",
  components: { MenuListItem },
  computed: {
    ...mapState({
      name: state => state.auth.nickname,
      role_name: state => state.auth.role_name,
      menuList: state=>state.leftMenuList
    }),
    isShowLeft: {
      get: function() {
        return this.$store.state.isShowLeft;
      },
      set: function(value) {
        this.$store.commit("setLeftSideBar", value);
      }
    }
  }
};
</script>
