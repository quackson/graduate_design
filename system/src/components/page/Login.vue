<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">Concept Map</div>
        </div>
        <div class="dsa">
            <div class="ms-title">数据结构与算法</div>
            <el-form ref="login" label-width="0px" class="ms-content">
                <div class="login-btn">
                    <el-button type="info" @click="signin('数据结构与算法','数据结构')">进入概念图</el-button>
                </div>
            </el-form>
        </div>
        <div class="mldl">
            <div class="ms-title">机器学习</div>
            <el-form ref="login" label-width="0px" class="ms-content">
                <div class="login-btn">
                    <el-button type="info" @click="signin('机器学习','机器学习')">进入概念图</el-button>
                </div>
            </el-form>
        </div>
        <div class="java">
            <div class="ms-title">Java编程</div>
            <el-form ref="login" label-width="0px" class="ms-content">
                <div class="login-btn">
                    <el-button type="info" @click="signin('Java','Java')">进入概念图</el-button>
                </div>
            </el-form>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        signin(map,concept) {
            this.$router.push('/concept/'+map+'/'+concept);
        },
    },
};
</script>

<style scoped>
.login-wrap {
    position: fixed;
    width:100%;
    height: 100%;
    background-size: 100%;
    background-repeat:no-repeat;
    background-attachment: fixed;
    background-image: url(../../assets/img/login5.png);
}
.head {
    width: 100%;
    height: 70px;
    background-color: #324157;
}
.head button {
    float: right;
    height: 36px;
    margin-left: 10px;
    margin-top: 15px;
}
.ms-title {
    width: 100%;
    line-height: 50px;
    text-align: center;
    font-size: 40px;
    color: #fff;
    border-bottom: 1px solid #ddd;
}
.ms-login {
    position: absolute;
    left: 50%;
    top: 0%;
    width: 350px;
    margin: 190px 0 0 -175px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.3);
    overflow: hidden;
}

.dsa {
    position: absolute;
    left: 25%;
    top: 20%;
    width: 350px;
    margin: 190px 0 0 -175px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.3);
    overflow: hidden;
}

.mldl {
    position: absolute;
    left: 50%;
    top: 20%;
    width: 350px;
    margin: 190px 0 0 -175px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.3);
    overflow: hidden;
}

.java {
    position: absolute;
    left: 75%;
    top: 20%;
    width: 350px;
    margin: 190px 0 0 -175px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.3);
    overflow: hidden;
}
.ms-content {
    padding: 30px 30px;
}
.login-btn {
    text-align: center;
}
.login-btn button {
    width: 100%;
    height: 36px;
    margin-bottom: 10px;
}
.login-tips {
    font-size: 12px;
    line-height: 30px;
    color: #fff;
}
</style>