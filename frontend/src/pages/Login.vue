<template>
  <q-layout>
    <q-page-container>
      <q-page
        class="fullscreen row"
        style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
      >
        <q-card
          bordered
          class="absolute-center col-xs-12 col-sm-6 col-md-4 col-lg-3 col-xl-2 shadow-16 bg-grey-3"
        >
          <q-tabs v-model="tabName" inline-label class="text-primary">
            <q-tab name="login" icon="face" label="登录" tabindex="-1" />
            <q-tab
              v-show="false"
              name="register"
              icon="how_to_reg"
              label="注册"
              tabindex="-1"
            />
          </q-tabs>
          <q-separator />
          <q-tab-panels v-model="tabName" animated>
            <q-tab-panel name="login">
              <div>
                <q-input
                  bottom-slots
                  clearable
                  v-model="loginForm.username"
                  label="用户名"
                  :rules="[val => !!val || '必须输入用户名']"
                  counter
                  :loading="isLoading"
                  tabindex="1"
                  @keyup.enter="login"
                >
                  <template v-slot:prepend>
                    <q-icon name="person" />
                  </template>
                </q-input>
                <q-input
                  :type="loginForm.showPassword ? 'text' : 'password'"
                  bottom-slots
                  clearable
                  v-model="loginForm.password"
                  :rules="[val => val.length >= 6 || '密码长度必须大于等于6']"
                  label="密码"
                  counter
                  :loading="isLoading"
                  tabindex="2"
                  @keyup.enter="login"
                >
                  <template v-slot:prepend>
                    <q-icon name="lock" />
                  </template>
                  <template v-slot:append>
                    <q-icon
                      :name="
                        loginForm.showPassword ? 'visibility' : 'visibility_off'
                      "
                      class="cursor-pointer"
                      @click="loginForm.showPassword = !loginForm.showPassword"
                      tabindex="-1"
                    />
                  </template>
                </q-input>
              </div>
              <q-card-actions class="justify-end">
                <q-btn
                  color="primary"
                  icon="login"
                  label="登录"
                  tabindex="3"
                  @click="login"
                />
              </q-card-actions>
            </q-tab-panel>
            <q-tab-panel name="register">
              <div>
                <q-input
                  bottom-slots
                  clearable
                  v-model="loginForm.username"
                  label="用户名"
                  :rules="[val => !!val || '必须输入用户名']"
                  counter
                  :loading="isLoading"
                  tabindex="1"
                  @keyup.enter="register"
                >
                  <template v-slot:prepend>
                    <q-icon name="person" />
                  </template>
                </q-input>
                <q-input
                  :type="loginForm.showPassword ? 'text' : 'password'"
                  bottom-slots
                  clearable
                  v-model="loginForm.password"
                  :rules="[val => val.length >= 6 || '密码长度必须大于等于6']"
                  label="密码"
                  counter
                  :loading="isLoading"
                  tabindex="2"
                  @keyup.enter="register"
                >
                  <template v-slot:prepend>
                    <q-icon name="lock" />
                  </template>
                  <template v-slot:append>
                    <q-icon
                      :name="
                        loginForm.showPassword ? 'visibility' : 'visibility_off'
                      "
                      class="cursor-pointer"
                      @click="loginForm.showPassword = !loginForm.showPassword"
                      tabindex="-1"
                    />
                  </template>
                </q-input>
              </div>
              <q-card-actions class="justify-end">
                <q-btn color="primary" icon="send" label="注册" tabindex="3" />
              </q-card-actions>
            </q-tab-panel>
          </q-tab-panels>
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  data() {
    return {
      tabName: "login",
      isLoading: false,
      loginForm: {
        username: "",
        password: "",
        showPassword: false
      },
      userToken: ""
    };
  },

  methods: {
    checkInput: function() {
      if (!this.loginForm.username || this.loginForm.password.length < 6) {
        this.$q.notify({
          type: "warning",
          position: "center",
          icon: "warning",
          message: "账号名或密码长度不满足要求!",
          timeout: 300
        });
        return false;
      } else {
        return true;
      }
    },
    login: function() {
      if (this.inputIsOk) {
        this.isLoading = true;
        this.$store
          .dispatch("auth/login", {
            username: this.loginForm.username,
            password: this.loginForm.password
          })
          .then(res => {
            this.isLoading = false;
            this.$q.notify({
              type: "positive",
              position: "center",
              icon: "announcement",
              message: "登录成功，正在跳转页面...",
              timeout: 300,
              progress: true
            });
            setTimeout(() => {
              if (this.$route.query.next){
                this.$router.push(decodeURIComponent(this.$route.query.next))
              }else{
                this.$router.push("/");
              }
            }, 1500);
          })
          .catch(err => {
            this.isLoading = false;
            this.$q.notify({
              type: "negative",
              position: "center",
              icon: "error",
              message: "账号或密码错误!!",
              timeout: 1000
            });
          });
      }
    }
  },
  computed: {
    inputIsOk: function() {
      if (!this.loginForm.username || this.loginForm.password.length < 6) {
        this.$q.notify({
          type: "warning",
          position: "center",
          icon: "warning",
          message: "账号名或密码长度不满足要求!",
          timeout: 300
        });
        return false;
      } else {
        return true;
      }
    }
  }
};
</script>
