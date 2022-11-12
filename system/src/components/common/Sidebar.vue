<template>
<div class="sidebar">
        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="collapse"
            background-color="#324157"
            text-color="#bfcbd9"
            active-text-color="#20a0ff"
            unique-opened
            router
        >
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index" :key="item.index">
                        <template slot="title">
                            <i :class="item.icon"></i>
                            <span slot="title">{{ item.title }}</span>
                        </template>
                        <template v-for="subItem in item.subs">
                            <el-submenu
                                v-if="subItem.subs"
                                :index="subItem.index"
                                :key="subItem.index"
                            >
                                <template slot="title">{{ subItem.title }}</template>
                                <el-menu-item
                                    v-for="(threeItem,i) in subItem.subs"
                                    :key="i"
                                    :index="threeItem.index"
                                >{{ threeItem.title }}</el-menu-item>
                            </el-submenu>
                            <el-menu-item
                                v-else
                                :index="subItem.index"
                                :key="subItem.index"
                            >{{ subItem.title }}</el-menu-item>
                        </template>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index" :key="item.index">
                        <i :class="item.icon"></i>
                        <span slot="title">{{ item.title }}</span>
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script>
import bus from '../common/bus';
export default {
    data() {
        return {
            collapse: false,
            items: [
                {
                    icon: 'el-icon-grape',
                    index: 'search?m=4&&k=Physics',
                    title: '机器学习与深度学习'
				},
                {
                    icon: 'el-icon-watermelon',
                    index: 'search?m=4&&k=math',
                    title: '数据结构与算法',
                },
                {
                    icon: 'el-icon-cherry',
                    index: 'map',
                    title: 'Java编程',
                }
            ]
        };
    },
	methods: {
		/*
		search_cat(e){
			//console.log(e.target);
			//console.log(e.currentTarget.getElementById("string"));
			console(e);
			var category=e;
				
		},		
		*/
	},
    computed: {
        onRoutes() {
			/*
			var url=this.$url;
			var k=0;
			var L=url.length;
			while(k<L)
			{
				if (url[k]=='#')
				{
					k++;
					break;
				}
			}
			url=url.substring(0,k);
            return url;
			*/
			var pre=this.$route.path.replace('/','');
			//console.log(pre);
			return pre;
        }
    },
    created() {
        // 通过 Event Bus 进行组件间通信，来折叠侧边栏
        bus.$on('collapse', msg => {
            this.collapse = msg;
            bus.$emit('collapse-content', msg);
        });
    }
};
</script>

<style scoped>
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    overflow-y: scroll;
    z-index:50;
    float: left;
}
.sidebar::-webkit-scrollbar {
    width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 350px;
}
.sidebar > ul {
    height: 100%;
}
</style>
