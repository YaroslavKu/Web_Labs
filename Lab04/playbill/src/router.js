import Vue from 'vue'
import Router from 'vue-router'
import Theatricals from "./views/Theatricals";

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: Theatricals
        },
        {
            path: '/theaters',
            component: () => import('./views/Theaters')
        },
        {
            path: '/theatrical/:id',
            component: () => import('./views/TheatricalDetail')
        },
        {
            path: '/login',
            component: () => import('./views/Login')
        },
        {
            path: '/register',
            component: () => import('./views/Register')
        }
    ]
})