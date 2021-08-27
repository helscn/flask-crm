import MainLayout from "layouts/MainLayout";

const routes = [
  {
    path: "/",
    meta: { title: "首页", icon: "home" },
    component: MainLayout,
    children: [
      {
        path: "",
        component: () => import("pages/Index.vue")
      },
      {
        path: "customers",
        meta: { title: "我的客户", icon: "people" },
        component: () => import("src/layouts/ContentLayout.vue"),
        children: [
          {
            path: "",
            meta: { keepAlive: true },
            component: () => import("pages/customers/ShowCustomers.vue")
          },

          {
            path: "new",
            meta: { title: "新建客户", icon: "add_circle" },
            component: () => import("pages/customers/NewCustomer.vue")
          },
          {
            path: "edit",
            meta: { title: "修改客户", icon: "edit" },
            component: () => import("pages/customers/EditCustomer.vue")
          }
        ]
      },
      {
        path: "products",
        meta: { title: "我的产品", icon: "business_center" },
        component: () => import("src/layouts/ContentLayout.vue"),
        children: [
          {
            path: "",
            meta: { keepAlive: true },
            component: () => import("pages/products/ShowProducts.vue")
          },

          {
            path: "new",
            meta: { title: "新建产品", icon: "add_circle" },
            component: () => import("pages/products/NewProduct.vue")
          },
          {
            path: "edit",
            meta: { title: "修改产品", icon: "edit" },
            component: () => import("pages/products/EditProduct.vue")
          }
        ]
      },
      {
        path: "suppliers",
        meta: { title: "我的供应商", icon: "support_agent" },
        component: () => import("src/layouts/ContentLayout.vue"),
        children: [
          {
            path: "",
            meta: { keepAlive: true },
            component: () => import("pages/suppliers/ShowSuppliers.vue")
          },

          {
            path: "new",
            meta: { title: "新供应商", icon: "add_circle" },
            component: () => import("pages/suppliers/NewSupplier.vue")
          },
          {
            path: "edit",
            meta: { title: "修改供应商信息", icon: "edit" },
            component: () => import("pages/suppliers/EditSupplier.vue")
          }
        ]
      },
      {
        path: "schedulers",
        meta: { title: "计划任务", icon: "scheduler" },
        component: () => import("src/layouts/ContentLayout.vue"),
        children: [
          {
            path: "",
            component: () => import("pages/schedulers/ShowSchedulers.vue")
          },
          {
            path: "new",
            meta: { title: "新建任务", icon: "add_circle" },
            component: () => import("pages/schedulers/NewScheduler.vue")
          }
        ]
      },
      {
        path: "upload",
        meta: { title: "上传文件" },
        component: () => import("pages/Upload.vue")
      }
    ]
  },
  {
    path: "/login",
    // 将 public 属性为 true 时表示该路由访问无需登录
    meta: { title: "登录", public: true },
    component: () => import("pages/Login.vue")
  },
  {
    path: "/pdf",
    meta: { public: true },
    component: () => import("pages/PdfPreview.vue")
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "*",
    component: () => import("pages/Error404.vue")
  }
];

export default routes;
