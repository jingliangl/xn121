export default [
    {
        path: '/cctv1',
        name: '001-1',
        label: 'cctv1',
        sideShow: false,
        component: resolve => require(['./pages/cctv1'], resolve)
    },
    {
        path: '/cctv2',
        name: '001-2',
        label: 'cctv2',
        sideShow: false,
        component: resolve => require(['./pages/cctv2'], resolve)
    },
    {
        path: '/cctv4',
        name: '001-3',
        label: 'cctv4',
        sideShow: false,
        component: resolve => require(['./pages/cctv4'], resolve)
    },
    {
        path: '/cctv7',
        name: '001-4',
        label: 'cctv7',
        sideShow: false,
        component: resolve => require(['./pages/cctv7'], resolve)
    },
    {
        path: '/lyws',
        name: '001-5',
        label: 'lyws',
        sideShow: false,
        component: resolve => require(['./pages/lyws'], resolve)
    },
    {
        path: '/detail',
        name: '002-1',
        label: 'detail',
        sideShow: false,
        component: resolve => require(['./pages/detail'], resolve)
    },
    // 其他
    {
        path: '*', // 其他页面，强制跳转到登录页面
        name: '999',
        redirect: '/'
    }
]
