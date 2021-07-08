<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs q-gutter-md">
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
    <q-table
      ref="productsTable"
      title="产品清单"
      :data="data"
      :columns="columns"
      row-key="id"
      selection="single"
      :selected.sync="selected"
      :pagination.sync="pagination"
      :filter="filter"
    >
      <template v-slot:top-right>
        <q-input
          borderless
          dense
          debounce="300"
          v-model="filter"
          placeholder="搜索产品"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input> </template
    ></q-table>
  </q-page>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      navigationActive: false,
      filter: "",
      selected: [],
      pagination: {},
      columns: [
        {
          name: "no",
          required: true,
          label: "产品代码",
          align: "left",
          field: row => row.no,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "name",
          required: true,
          label: "产品名称",
          align: "center",
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "spec",
          required: false,
          label: "产品规格",
          align: "center",
          field: row => row.spec,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "description",
          required: false,
          label: "产品描述",
          align: "left",
          field: row => row.description,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "moq",
          required: true,
          label: "MOQ",
          align: "right",
          field: row => row.moq,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "purchase_price",
          required: true,
          label: "采购价格",
          align: "right",
          field: row => row.purchase_price,
          format: val => `¥ ${val.toFixed(2)}`,
          sortable: true
        },
        {
          name: "profit_rate",
          required: true,
          label: "利润率",
          align: "right",
          field: row => row.profit_rate,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "comment",
          required: false,
          label: "备注",
          align: "center",
          field: row => row.comment,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "created_date",
          required: true,
          label: "创建日期",
          align: "center",
          field: row => row.created_date,
          sortable: true
        }
      ]
    };
  },
  computed: {
    // ...mapState({
    //   data: state => state.products.data
    // })
    ...mapGetters({
      data: "products/validProducts"
    })
  }
};
</script>
