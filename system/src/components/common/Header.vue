<template>
  <div class="header">
    <div class="home-btn" @click="homeScreenChange">
      <i class="el-icon-s-home"></i>
    </div>

    <div class="logo">Concept Map</div>
    
    <div class="header-right">
      <div class="header-user-con">
        <!-- 全屏显示 -->
        <div class="btn-fullscreen" @click="handleFullScreen">
          <el-tooltip
            effect="dark"
            :content="fullscreen ? `取消全屏` : `全屏`"
            placement="bottom"
          >
            <i class="el-icon-rank"></i>
          </el-tooltip>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import bus from "../common/bus";
export default {
  data() {
    return {
      collapse: false,
      fullscreen: false,
      name: "linxin",
      message: 2,
      search: "",
      select: "",
      userImage: "",
    };
  },
  computed: {
    username() {
      let username = localStorage.getItem("ms_username");
      return username ? username : this.name;
    }
  },
  methods: {
    // 用户名下拉菜单选择事件
    handleCommand(command) {
      if (command !== "loginout") {
        this.$router.push({ path: `/account/${command}` });
      } else {
        localStorage.removeItem("ms_username");
        this.$router.push("/login");
      }
    },
	//跳转到搜索页面
	gotosearchpage()	{
	
		var keyword=this.search;
		var method=this.select;
		 this.$router.push({
          path: '/search',
          query: {
            k: keyword,
			m:method,
          }
        });	
	
	//this.$router.push("/search");	
	},
    //主页
    homeScreenChange() {
      this.$router.push("/home");
    },
    // 侧边栏折叠
    collapseChage() {
      this.collapse = !this.collapse;
      bus.$emit("collapse", this.collapse);
    },
    // 全屏事件
    handleFullScreen() {
      let element = document.documentElement;
      if (this.fullscreen) {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        } else if (document.webkitCancelFullScreen) {
          document.webkitCancelFullScreen();
        } else if (document.mozCancelFullScreen) {
          document.mozCancelFullScreen();
        } else if (document.msExitFullscreen) {
          document.msExitFullscreen();
        }
      } else {
        if (element.requestFullscreen) {
          element.requestFullscreen();
        } else if (element.webkitRequestFullScreen) {
          element.webkitRequestFullScreen();
        } else if (element.mozRequestFullScreen) {
          element.mozRequestFullScreen();
        } else if (element.msRequestFullscreen) {
          // IE11
          element.msRequestFullscreen();
        }
      }
      this.fullscreen = !this.fullscreen;
    }
  },
  mounted() {
    if (document.body.clientWidth < 1500) {
      this.collapseChage();
    }
  }
};
</script>
<style scoped>
.header {
  background-color: #324157;
  box-sizing: border-box;
  height: 70px;
  position: fixed;
  top: 0px;
  width: 100%;
  font-size: 22px;
  color: #fff;
  z-index: 50;
}
.collapse-btn {
  float: left;
  padding: 0 10px;
  cursor: pointer;
  line-height: 70px;
  font-size: 30px;
}
.home-btn {
  float: left;
  padding: 0 5px;
  cursor: pointer;
  line-height: 70px;
  font-size: 30px;
}
.header .logo {
  float: left;
  padding: 0 5px;
  width: 250px;
  cursor: pointer;
  line-height: 70px;
}
.searchbar {
  float: left;
  padding-left: 10%;
  width: 40%;
  cursor: pointer;
  line-height: 70px;
}
.el-select {
  width: 150px;
}
.header-right {
  float: right;
  padding-right: 2%;
  width: 10%;
}
.header-user-con {
  display: flex;
  height: 70px;
  align-items: center;
}
.btn-fullscreen {
  align-items: center;
  transform: rotate(45deg);
  margin-right: 5px;
  font-size: 30px;
}
.btn-fullscreen {
  position: relative;
  width: 30px;
  height: 30px;
  text-align: center;
  border-radius: 15px;
  cursor: pointer;
}
.user-name {
  padding-left: 5%;
}
.user-avator {
  padding-left: 5%;
}
.user-avator img {
  display: block;
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
.el-dropdown-link {
  color: #fff;
  cursor: pointer;
}
.el-dropdown-menu__item {
  text-align: center;
}
</style>
