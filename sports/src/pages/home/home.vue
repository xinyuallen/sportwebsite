<template>
  <div class="home">
    <div class="bigPic">
      <div :style="styleObj">
        <img :style="styleObj" v-lazy="bigPic.home_imgUrl" alt="">
      </div>
      <div class="desc">
        <h2>{{bigPic.home_title}}</h2>
        <p>{{bigPic.home_desc}}</p>
        <div>
          <a href="javascript:;">
            <span class="shop">DESCRIPTION</span>
          </a>
        </div>
      </div>
    </div>
    <div class="bigPic" v-for="(item, index) in bigCategoryArr" :key="index">
      <div :style="styleObj">
        <img :style="styleObj" v-lazy="item.category_imgUrl">
      </div>
      <div class="desc">
        <h2>{{item.category_name}}</h2>
        <p>{{item.category_desc}}</p>
        <div>
          <a href="javascript:;" @click="showCategory(item.category_name)">
            <span class="shop">DESCRIPTION</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { getHomePic, getHomeCategory } from '@/http/http.js';
let baseUrl = 'http://202.195.167.248/media/';
let HEIGHT = document.body.clientHeight;
export default {
  name: '',
  data() {
    return {
      styleObj: {height: `${HEIGHT - 107 - 107}px`},
      bigPic:{},
      bigCategoryArr: []
    }
  },
  methods:{
    showCategory(categoryName){
      this.$router.push({name:'category', params:{categoryName}});
    }
  },
  created(){
    /*获取大图*/
    getHomePic().then(res => {
      this.bigPic = res.data;
      this.bigPic.home_imgUrl = baseUrl + res.data.home_imgUrl;
    }).catch(err => {
      alert('网络错误！')
    })
    /*获取category大图*/
    getHomeCategory().then(res => {
      this.bigCategoryArr = res.data;
      for(let i=0; i<res.data.length; i++){
        this.bigCategoryArr[i].category_imgUrl = baseUrl + res.data[i].category_imgUrl;
      }
    }).catch(err => {
      alert('网络错误！')
    })
  }
}
</script>
<style scoped lang="scss">
  .home{
    padding-top: 107px;
    .bigPic{
      text-align: center;
      margin-bottom: 15px;
      img{
        width: 100%;
      }
      .desc{
        margin: 0 auto;
        margin-top: 50px;
        width: 50%;
        p{
          color: #111;
        }
        .shop{
          display: inline-block;
          margin: 5px 0;
          padding: 0 20px;
          height: 40px;
          line-height: 40px;
          background-color: #000;
          color: #fff;
          font-size: .8em;
          letter-spacing: -0.1em;
        }
      }
    }
  }
</style>
