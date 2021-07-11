<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs q-gutter-md">
    <template>
      <q-btn
        label="新建产品"
        icon="add_circle_outline"
        @click="$router.push('/products/new')"
        color="primary"
      />
      <q-btn
        label="修改产品"
        icon="edit"
        @click="$router.push('/products/edit')"
        color="primary"
      />
      <q-btn
        label="删除产品"
        icon="delete_forever"
        @click="removeProducts"
        color="primary"
      />
      <q-btn
        label="导出产品"
        icon="file_download"
        @click="$router.push('/products/download')"
        color="primary"
      />
      <q-btn
        label="导入产品"
        icon="file_upload"
        @click="$router.push('/products/upload')"
        color="primary"
      />
    </template>
    <q-table
      ref="productsTable"
      :data="data"
      :columns="columns"
      row-key="id"
      selection="multiple"
      :selected.sync="selected"
      :pagination.sync="pagination"
      :filter="filter"
      :visible-columns="visibleColumns"
      @row-dblclick="showProductCard"
      table-header-class="bg-grey-4"
    >
      <template v-slot:top>
        <q-input
          color="black"
          dense
          debounce="300"
          v-model="filter"
          placeholder="搜索产品"
        >
          <template v-slot:prepend>
            <q-icon name="search" />
          </template>
          <template v-if="filter" v-slot:append>
            <q-icon name="close" @click="filter = ''" class="cursor-pointer" />
          </template>
        </q-input>
        <q-space />
        <q-select
          v-model="visibleColumns"
          multiple
          outlined
          dense
          options-dense
          display-value="列选择"
          emit-value
          map-options
          :options="columns"
          option-value="name"
          options-cover
          style="min-width: 150px"
        />
      </template>
    </q-table>
    <q-dialog v-model="isShowCard">
      <q-card class="my-card">
        <q-card-section>
          <div class="row no-wrap items-center">
            <div class="col">
              <q-badge
                class="text-subtitle2"
                color="accent"
                align="middle"
                :label="currentProduct.no"
              />
              <span class="q-ml-md text-subtitle1">
                {{ currentProduct.name }}</span
              >
            </div>
            <div
              class="col-auto text-grey-6 text-subtitle1 q-pt-none row no-wrap items-center"
            >
              {{ currentProduct.spec }}
            </div>
          </div>
        </q-card-section>
        <q-img :src="currentProduct.thumbnail" />
        <q-card-section>
          {{ currentProduct.description }}
        </q-card-section>

        <q-separator />

        <q-card-actions align="right">
          <q-btn v-close-popup flat color="primary" label="关闭" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      showProduct: true,
      filter: "",
      selected: [],
      pagination: { sortBy: null, descending: false, page: 1, rowsPerPage: 5 },
      columns: [
        {
          name: "no",
          label: "产品代码",
          align: "left",
          field: row => row.no,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "name",
          label: "产品名称",
          align: "center",
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "spec",
          label: "产品规格",
          align: "center",
          field: row => row.spec,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "description",
          label: "产品描述",
          align: "left",
          field: row => row.description,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "moq",
          label: "MOQ",
          align: "right",
          field: row => row.moq,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "purchase_price",
          label: "采购价格",
          align: "right",
          field: row => row.purchase_price,
          format: val => `¥ ${val.toFixed(2)}`,
          sortable: true
        },
        {
          name: "profit_rate",
          label: "利润率",
          align: "right",
          field: row => row.profit_rate,
          format: val => `${val * 100}%`,
          sortable: true
        },
        {
          name: "thumbnail",
          label: "缩略图",
          align: "center",
          field: row => row.thumbnail,
          format: val => (val ? "\u2705" : "\u274C"),
          sortable: true
        },
        {
          name: "comment",
          label: "备注",
          align: "center",
          field: row => row.comment,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "created_date",
          label: "创建日期",
          align: "center",
          field: row => row.created_date,
          sortable: true
        }
      ],
      visibleColumns: [
        "no",
        "name",
        "spec",
        "description",
        "moq",
        "purchase_price",
        "profit_rate",
        "thumbnail"
      ],
      currentProduct: {},
      isShowCard: false
    };
  },
  methods: {
    showProductCard(evt, row, index) {
      this.currentProduct = row;
      this.isShowCard = true;
    },
    removeProducts() {
      this.$q
        .dialog({
          title: "确认",
          message: "确认要删除当前选定的产品吗？注意该操作无法恢复！",
          cancel: true,
          persistent: true,
          focus: "cancel"
        })
        .onOk(() => {
          alert("Deleted!");
        })
        .onCancel(() => {});
    }
  },
  computed: {
    ...mapGetters({
      data: "products/validProducts"
    })
  },
  created() {
    this.$store.dispatch("products/fetchProducts").catch(err => {
      this.$q.notify({
        type: "negative",
        position: "top",
        icon: "warning",
        message: "无法获取产品数据，请确认网络连接是否正常。"
      });
    });
  }
};
</script>

<style>
.my-card {
  max-width: 100%;
  min-width: 400px;
}
</style>
