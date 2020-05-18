<template>
  <div class="header">
    <nav class="nav">
      <ul class="ul-left">
        <li v-for='(item, index) in navList' :key="index">
          <a :href="item.brandurl">{{item.brandname}}</a>
        </li>
      </ul>
      <ul class="ul-right">
        <!-- <li class="li-help">
          <a href="">help</a>
          help部分
          <ul class="ul-help">
            <li v-for="(item, index) in helpList" :key="index">
              <a :href="item.url">
                {{item.name}}
              </a>
            </li>
          </ul>
        </li> -->
        <li>
          <a href="javascript:;" @click="changeLang">
            <img src="../../assets/au_sml.png" alt="">
          </a>
        </li>
      </ul>
    </nav>
    <div class="category">
      <a class="logo" href="/"><img src="../../../static/Austar-favicon.jpg" alt=""/></a>
      <ul>
        <li v-for="(item, index) in categoryList" :key="index">
          <span class="categoryName" @click="toCategory(item.categoryName)">{{item.categoryName}}</span>
          <!-- 下拉分类 -->
          <div class="dropdown" v-if="item.showType === 'L' ? true : false"><Dropdown1 :subCategoryList="item.subCategory"></Dropdown1></div>
          <div class="dropdown" v-if="item.showType === 'T' ? true : false"><Dropdown2 :subCategoryList="item.subCategory"></Dropdown2></div>
          <div class="dropdown" v-if="item.showType === 'B' ? true : false"><Dropdown3 :subCategoryList="item.subCategory"></Dropdown3></div>
        </li>
      </ul>
      <div class="searchDiv">
        <div class="search">
          <img src="../../assets/search.png" alt="">
          <input
          type="text"
          v-model="searchText"
          placeholder="Search"
          @keyup.enter="searchCategory">
          <span :class="searchText ? 'hover' : ''" class="delete" @click="deleteText"><i></i></span>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { getBrand, getHomeSubCategory } from '@/http/http.js';
import Dropdown1 from '@/components/dropdown/dropdown1.vue';
import Dropdown2 from '@/components/dropdown/dropdown2.vue';
import Dropdown3 from '@/components/dropdown/dropdown3.vue';
export default {
  name: 'sHeader',
  data() {
    return {
      categoryList: [],
      navList: [],
      helpList: [
        {name: 'Nike', url:''},
        {name: 'Nike', url:''},
        {name: 'Nike', url:''},
        {name: 'Nike', url:''},
        {name: 'Nike', url:''},
        {name: 'Nike', url:''},
        {name: 'Nike', url:''},
      ],
      searchText: ''
    }
  },
  components:{
    Dropdown2,
    Dropdown3,
    Dropdown1
  },
  methods:{
    changeLang(){
      console.log("111");
      this.$router.push({name: 'language'});
    },
    deleteText(){
      this.searchText = '';
    },
    /*转到对应的商品分类*/
    searchCategory(){
      if(this.searchText){
        this.$router.push({name:'category', params:{categoryName: this.searchText}});
        this.searchText = '';
      }
    },
    toCategory(categoryName){
      this.$router.push({name:'category', params:{categoryName}});
    }
  },
  created(){
    /*获取品牌*/
    getBrand().then(res => {
      this.navList = res.data;
    }).catch(err => {
      alert('网络错误！')
    })
    /*获取首页分类与子分类*/
    getHomeSubCategory().then(res => {
      this.categoryList = res.data;
    }).catch(err => {
      alert('网络错误！')
    })
  }
}
</script>
<style scoped lang="scss">
  @keyframes changeWid
  {
    0% {width: 167px;}
    100% {width: 200px;}
  }
  @keyframes changeColor
  {
    from {border-color: #eee;}
    to {border-color: #999;}
  }
  .header{
    position: fixed;
    z-index: 1000;
    font-size: 16px;
    line-height: 1.5em;
    width: 100%;
    min-width: 1200px;
    .nav{
      position: relative;
      z-index: 999;
      height: 39px;
      line-height: 39px;
      border-bottom: 1px solid #E5E5E5;
      background: white;
      color: #8D8D8D;
      ul{
        position: absolute;
        li{
          display: inline-block;
          padding: 0 32px;
          font-size: 12px;
          a{
            color: inherit;
            &:hover{
              color: #111;
            }
          }
        }
      }
      .ul-left{
        top: -2px;
        li{
          border-right: 1px solid #E5E5E5;
        }
      }
      .ul-right{
        right: 13px;
        margin-top: -3px;
        li{
          cursor: pointer;
          padding: 0 11px;
          font-size: 12px;
          border-bottom: 2px solid transparent;
          img{
            width: 14px;
            height: 10px;
          }
        }
        .li-help{
          &:hover{
            border-color: #111;
          }
        }
      }
      .li-help{
        &:hover{
          ul{
            visibility: visible;
          }
        }
        /* help下拉框 */
        ul{
          position: absolute;
          margin-top: 2px;
          visibility: hidden;
          background-color: white;
          border: 1px solid #E5E5E5;
          border-top: none;
          padding: 26px 32px 25px;
          left: -50%;
          /* 防止继承 */
          line-height: 1;
          li{
            border: 0;
            a{
              display: inline-block;
              height: 20px;
              line-height: 20px;
            }
          }
        }
      }
    }
    .category{
      height: 68px;
      background-color: #fff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
      border-bottom: 1px solid #E5E5E5;
      .logo{
        margin-left: 40px;
        img{
          width: 40px;
          height: 40px;
        }
      }
      ul{
        height: 100%;
        margin-left: 40px;
        li{
          display: inline-block;
          margin-left: 25px;
          border-bottom: 2px solid transparent;
          height: 100%;
          line-height: 68px;
          cursor: pointer;
          .categoryName{
            text-transform:uppercase;
            font-weight: 600;
          }
          .dropdown{
            visibility: hidden;
            padding-top: 20px;
          }
          &:hover{
            border-color: #000;
            .dropdown{
              visibility: visible;
            }
          }
        }
      }
      .searchDiv{
        margin-right: 20px;
        width: 250px;
        display: flex;
        justify-content: flex-end;
        .search{
          border: 1px solid #eee;
          display: flex;
          align-items: center;
          justify-content: flex-end;
          height: 38px;
          &:hover{
            animation: changeColor 1s forwards ease-in-out;
          }
          img{
            display: inline-block;
            width: 16px;
            margin: 0 8px 0 12px;
          }
          input{
            padding: 5px;
            border: 0;
            outline:none;
            &:hover{
              animation: changeWid 1s forwards ease-in-out;
            }
          }
          .delete{
            padding-right: 10px;
            cursor: pointer;
            visibility: hidden;
            i{
              &:before{
                content: '×';
                width: 32px;
                height: 32px;
              }
            }
          }
          .hover{
            visibility: visible;
          }
        }
      }
    }
  }
</style>
