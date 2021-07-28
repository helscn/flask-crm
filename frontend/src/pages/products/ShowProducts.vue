<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs q-gutter-md">
    <q-btn-group rounded push>
      <q-btn
        label="新建"
        icon="add_circle_outline"
        @click="$router.push('/products/new')"
        color="primary"
      />
      <q-btn
        label="修改"
        :disable="selected.length !== 1"
        icon="edit"
        @click="
          $router.push({
            path: '/products/edit',
            query: { id: selected[0].id }
          })
        "
        color="primary"
      />
      <q-btn
        label="删除"
        :disable="selected.length === 0"
        rounded
        icon="delete_forever"
        @click="removeProducts"
        color="primary"
      />
    </q-btn-group>
    <q-btn-group rounded>
      <q-btn
        label="导出"
        icon="file_download"
        @click="$router.push('/products/download')"
        color="primary"
      />
      <q-btn
        label="导入"
        icon="file_upload"
        @click="$router.push('/products/upload')"
        color="primary"
      />
    </q-btn-group>
    <q-btn
      rounded
      color="primary"
      icon="add_shopping_cart"
      label="加入购物车"
      @click="addCart"
    />

    <div>
      <q-tabs
        v-model="productsFilter"
        align="left"
        inline-label
        class="bg-grey-4 text-primary shadow-2"
        :breakpoint="300"
      >
        <q-tab name="all" label="所有产品" icon="business_center" />
        <q-tab name="valid" label="上架产品" icon="visibility" />
        <q-tab name="unvalid" label="下架产品" icon="visibility_off" />
      </q-tabs>
      <q-table
        ref="productsTable"
        :loading="loading"
        :data="data"
        :columns="columns"
        row-key="id"
        selection="multiple"
        :selected.sync="selected"
        :pagination.sync="pagination"
        :filter="filter"
        :visible-columns="visibleColumns"
        @row-dblclick="showProductCard"
        table-header-class="bg-grey-2"
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
              <q-icon
                name="close"
                @click="filter = ''"
                class="cursor-pointer"
              />
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
    </div>

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
          <div class="text-wrapper">{{ currentProduct.description }}</div>
        </q-card-section>

        <q-separator />

        <q-card-actions align="right">
          <q-btn v-close-popup flat color="primary" label="关闭" />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-page-sticky position="bottom-right" :offset="cartPos">
      <q-fab
        glossy
        external-label
        label-position="left"
        label="购物车"
        color="primary"
        icon="shopping_cart"
        direction="up"
        :disable="draggingCart"
        v-touch-pan.prevent.mouse="moveCart"
      >
        <template v-slot:tooltip>
          <q-badge color="orange" text-color="black" floating>{{
            cartItemsCount
          }}</q-badge>
        </template>
        <q-fab-action
          external-label
          label-position="left"
          label="创建询价单"
          color="primary"
          icon="description"
        />
        <q-fab-action
          external-label
          label-position="left"
          label="创建订单"
          color="primary"
          icon="request_quote"
        />
      </q-fab>
    </q-page-sticky>
  </q-page>
</template>

<script>
import { mapState, mapGetters } from "vuex";

export default {
  data() {
    return {
      productsFilter: "valid",
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
          name: "category",
          label: "产品分类",
          align: "center",
          field: row => row.category,
          format: val => val || "(无)",
          sortable: true
        },
        {
          name: "supplier",
          label: "产品供应商",
          align: "center",
          field: row => row.supplier,
          format: val => val || "(无)",
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
          label: "参考利润率",
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
          name: "created_date",
          label: "创建日期",
          align: "center",
          field: row => row.created_date,
          sortable: true
        },
        {
          name: "modified_date",
          label: "修改日期",
          align: "center",
          field: row => row.modified_date,
          sortable: true
        },
        {
          name: "valid",
          label: "上架产品",
          align: "center",
          field: row => (row.valid ? "\u2705" : "\u274C"),
          sortable: true
        }
      ],
      visibleColumns: [
        "no",
        "name",
        "spec",
        "category",
        "supplier",
        "moq",
        "purchase_price",
        "profit_rate",
        "modified_date",
        "valid"
      ],
      currentProduct: {},
      isShowCard: false,
      cartPos: [40, 40],
      draggingCart: false
    };
  },
  watch: {
    productsFilter: function(val, oldVal) {
      this.$store.commit("products/setProductsFilter", val);
      this.selected = [];
    }
  },
  methods: {
    showProductCard(evt, row, index) {
      this.currentProduct = row;
      this.isShowCard = true;
    },
    removeProducts() {
      if (this.selected.length === 0) {
        this.$q.notify({
          type: "warning",
          position: "top",
          icon: "warning",
          timeout: 2000,
          message: "请先选择需要删除的产品项目。"
        });
      } else {
        this.$q
          .dialog({
            title: "确认",
            message: "确认要删除当前选定的产品吗？注意该操作无法恢复！",
            cancel: true,
            persistent: true,
            focus: "cancel"
          })
          .onOk(() => {
            let ids = this.selected.map(v => v.id);
            this.$axios
              .delete("/api/products", {
                data: {
                  id: ids
                }
              })
              .then(res => {
                this.$store.dispatch("products/fetchProducts");
              });
          });
      }
    },
    moveCart(ev) {
      this.draggingCart = ev.isFirst !== true && ev.isFinal !== true;
      this.cartPos = [
        this.cartPos[0] - ev.delta.x,
        this.cartPos[1] - ev.delta.y
      ];
    },
    addCart() {
      this.selected.forEach(el => {
        this.$store.commit("products/addCartItem", el);
      }, this);
      this.selected = [];
    }
  },
  computed: {
    ...mapState({
      loading: state => state.products.loading
    }),
    ...mapGetters({
      data: "products/filteredProducts",
      cartItemsCount: "products/cartItemsCount"
    })
  },
  created: function() {
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
.text-wrapper {
  white-space: pre-wrap;
}
</style>
