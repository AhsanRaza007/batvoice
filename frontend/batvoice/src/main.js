





import VueRouter from 'vue-router'
import Vue from 'vue'
import App from './App.vue'
import Login from './components/Login'
import Register from './components/Register'
import Home from './components/Home'
import UsersLanding from './components/UsersLanding'
Vue.config.productionTip = false

Vue.use(VueRouter);

const routes = [
  { path: '/login', component: Login, name:'Login'},
  { path: '/register', component: Register, name:'Register'},
  { path: '/', component: Home, name:"Home"},
  { path: '/audio', component:UsersLanding, name:"User"}
]

const router = new VueRouter({
  routes,
  mode:'history'
})
new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
