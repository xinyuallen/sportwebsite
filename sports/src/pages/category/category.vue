<template>
  <div class="categoryList">
    <div class="title">{{$route.params.categoryName}}</div>
    <div v-if="productList.length === 0 ? true : false" class="noMore">No goods in this category</div>
    <div class="list">
      <a href="javascript:;" class="product" v-for="(item, index) in productList" :key="index">
        <img v-lazy="item.product_img" alt="">
        <div class="desc">
          <div>{{item.product_desc1}}</div>
          <div>{{item.product_desc2}}</div>
        </div>
      </a>
    </div>
    <div v-if="moreBool" class="more" @click="loadMore">Load more</div>
    <div v-else="!moreBool" class="more no-more">No more</div>
  </div>
</template>
<script>
import { getProductList } from '@/http/http.js';
let baseUrl = 'http://202.195.167.248/media/';
export default {
  name: 'Category',
  data() {
    return {
      productList:[],
      moreBool: true
    }
  },
  methods:{
    loadMore(){
      console.log(this.productList.length);
      this.getProductList(this.productList.length, 4);
    },
    getProductList(start, limit){
      getProductList({
        categoryName: this.$route.params.categoryName,
        start,
        limit
      }).then(res =>{
        if(res.data.length > 0){
          for(let i=0; i<res.data.length; i++){
            res.data[i].product_img = baseUrl + res.data[i].product_img;
          }
          this.productList = this.productList.concat(res.data);
        }else{
          /*无更多商品*/
          /*alert('no more!')*/
          this.moreBool = false;
        }
      }).catch(err => {
        alert('网络错误！')
      })
    }
  },
  created(){
    this.getProductList(this.productList.length,12);
  },
  watch: {
    /*如果路由有变化，会再次执行该方法*/
    "$route": function(){
      this.productList = [];
      this.moreBool = true;
      this.getProductList(this.productList.length,12);
    }
  }
}
</script>
<style scoped lang="scss">
  .categoryList{
    padding: 107px 100px 0;
    background-color: #f6f7f8;
    display: flex;
    flex-direction: column;
    align-items: center;
    .title{
      height: 100px;
      line-height: 100px;
      font-size: 50px;
      color: #41535D;
      margin: 20px 0;
      text-transform:capitalize;
    }
    .noMore{
      font-size: 30px;
    }
    .list{
      display: flex;
      flex-wrap: wrap;
      padding: 10px;
      padding-right: 0;
      width: 100%;
      .product{
        margin-right: 10px;
        margin-bottom: 20px;
        background-color: #fff;
        width: calc((100% - 50px)/4);
        padding: 20px 10px;
        text-align: center;
        img{
          width: 200px;
          height: 200px;
          transition: transform 0.3s ease-in-out;
          &:hover{
            transform: scale(1.1, 1.1);
          }
        }
        .desc{
          height: 60px;
          margin-top: 10px;
          color: #41535D;
        }
      }
    }
    .more{
      width: 150px;
      height: 45px;
      line-height: 45px;
      background-color: #43AAE0;
      text-align: center;
      cursor: pointer;
      margin-bottom: 20px;
      color: #fff;
      font-weight: 500;
      &:hover{
        background-color: #62c2f4;
      }
    }
    .no-more{
      cursor: default;
      &:hover{
        background-color: #43AAE0;
      }
    }
  }
</style>
