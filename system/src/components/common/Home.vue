<template>
    <div class="wrapper">
        <v-head></v-head>
        <div class="content-box" :class="{'content-collapse':collapse}">
                <transition name="move" mode="out-in">
                        <router-view></router-view>
                </transition>
        </div>
    </div>
</template>

<script>

import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent
]);
import vHead from './Header.vue';
import bus from './bus';
export default {
    data() {
        return {
            collapse: false
        };
    },
    components: {
        vHead
    },
    created() {
        bus.$on('collapse-content', msg => {
            this.collapse = msg;
        });
    }
};
</script>

<style scoped>
.content-box{
    right: 30px;
    top: 70px;
    bottom: 0;
    padding-bottom: 30px;
    position: absolute;
    left: 50px;
    transition: left .3s ease-in-out;
}
.content-collapse{
    left: 60px;
}
</style>
