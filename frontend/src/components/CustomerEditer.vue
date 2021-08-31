<template>
  <div class="q-py-lg row justify-center">
    <q-form
      ref="myForm"
      class="col-xs-12 col-sm-8 col-md-6 col-xl-4 shadow-3 q-pa-md"
    >
      <div class="row justify-between q-gutter-md">
        <q-input
          class="col"
          filled
          v-model.trim="company"
          label="公司名称*"
          lazy-rules
          :rules="[val => (val && val.length > 0) || '请输入公司名称']"
        />
        <div class="col row items-center q-mb-sm">
          <span>有效客户：</span>
          <q-toggle v-model="valid" />
        </div>
      </div>
      <div class="row justify-between q-gutter-md">
        <q-input class="col" filled v-model.trim="country" label="国家" />
        <div class="col row items-center">
          <span class="row">客户评级：</span>
          <q-rating
            class="row"
            v-model="importance"
            size="2em"
            :max="5"
            color="orange"
          />
        </div>
      </div>
      <div class="row justify-between q-gutter-md q-my-sm">
        <q-input class="col" filled v-model.trim="website" label="网站" />
      </div>

      <div class="row justify-between q-gutter-md q-my-sm">
        <q-input
          class="col"
          filled
          v-model.trim="address"
          label="地址"
          autogrow
        />
      </div>
      <div class="row justify-between q-gutter-md">
        <div class="col">
          <div class="text-grey-7 text-subtitle1">备注</div>
          <div>
            <q-editor v-model="comment" min-height="8rem" />
          </div>
        </div>
      </div>

      <div class="row justify-around q-pt-md">
        <q-btn color="primary" icon="save" label="保存" @click="save" />
        <q-btn color="primary" icon="cancel" label="取消" @click="cancel" />
      </div>
    </q-form>
  </div>
</template>

<script>
export default {
  name: "CustomerEditer",
  props: {
    data: Object
  },
  data() {
    return {
      id: 0,
      company: "",
      importance: 0,
      country: "",
      address: "",
      website: "",
      comment: "",
      valid: true
    };
  },
  watch: {
    thumbnail: function(val, oldVal) {
      this.thumbnail_url = window.URL.createObjectURL(val);
    },
    data: {
      handler: function(val, oldval) {
        if (val) {
          this.id = val.id || this.id;
          this.company = val.company || this.company;
          this.importance = val.importance || this.importance;
          this.country = val.country || this.country;
          this.address = val.address || this.address;
          this.website = val.website || this.website;
          this.comment = val.comment || this.comment;
          this.valid = val.valid === undefined ? this.valid : !!val.valid;
        }
      },
      immediate: true
    }
  },
  methods: {
    cancel() {
      this.$emit("cancel");
    },
    save() {
      this.$refs.myForm.validate().then(success => {
        if (success) {
          let data = {
            id: this.id,
            company: this.company,
            importance: this.importance,
            country: this.country,
            address: this.address,
            website: this.website,
            comment: this.comment,
            valid: this.valid
          };
          this.$emit("save", data, this.id);
        } else {
          this.$q.notify({
            type: "negative",
            position: "top",
            icon: "error",
            message: "数据错误，请检查表单是否填写正确!",
            timeout: 1000
          });
        }
      });
    }
  }
};
</script>
