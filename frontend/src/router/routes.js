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
        path: "projects",
        meta: { title: "我的项目", icon: "widgets" },
        component: () => import("pages/ProjectsView.vue")
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
        path: "upload",
        meta: { title: "上传文件" },
        component: () => import("pages/Upload.vue")
      }
    ]
  },
  {
    path: "/login",
    component: () => import("pages/Login.vue")
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "*",
    component: () => import("pages/Error404.vue")
  }
];

export default routes;
