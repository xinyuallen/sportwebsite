<template>
  <div class="footer" :style="styleObj">
    <div class="extra">
      <ul>
        <li>
          <a href="javascript:;">
            PRODUCT HIGHLIGHT
          </a>
        </li>
        <li>
          <a href="javascript:;" @click="changeBool('SEBool')">Strength Equipment</a>
          <transition name="fade">
            <div v-show="boolList.SEBool">From Dumbbell to Gym Stations, everything thing you need for muscle building is here.</div>
          </transition>
        </li>
        <li>
          <a href="javascript:;" @click="changeBool('FBool')">Functional</a>
          <transition name="fade">
            <div v-show='boolList.FBool'>An extensive range of equipment and tools for Cardio Workout, Resistance Training, CrossFit Training, Boxing/MMA, Yoga/Aerobics and so on.</div>
          </transition>
        </li>
        <li>
          <a href="javascript:;" @click="changeBool('OBool')">Outdoor</a>
          <transition name="fade">
            <div v-show='boolList.OBool'>One of our most successful product lines. Proven to be popular in the US and European Market.</div>
          </transition>
        </li>
        <li>
          <a href="javascript:;" @click="changeBool('ABool')">Accessories</a>
          <transition name="fade">
            <div v-show='boolList.ABool'>Thousands of fitness accessories to choose from. You name it, we have it. And if we don't, we probably have something better to offer.</div>
          </transition>
        </li>
      </ul>
      <ul>
        <li>
          <a href="javascript:;" @click="changeBool('AUBool')">
            ABOUT US
          </a>
        </li>
        <li>
          <transition name="fade">
            <div v-show='boolList.AUBool'>Prooudly serving the fitness industry for over 30 years. Austar has always been a reliable equipment manufacturer and supplier to many well-know sports retail giants. To Australia, we may be new. But to the fitness world, we are always there.</div>
          </transition>
        </li>
        <li>
          <a href="javascript:;" @click="changeBool('OPBBool')">Our Product Base</a>
          <transition name="fade">
            <div v-show='boolList.OPBBool'>With production bases across Asia and 2,000 active workers, we are able to meet the various needs and requirements of our clients.</div>
          </transition>
        </li>
        <li>
          <a href="javascript:;" @click="changeBool('OPBool')">Our Product</a>
          <transition name="fade">
            <div v-show='boolList.OPBool'>Engineered and repeatedly improved by listening to our clients, our products are proven to be satisfctory in terms of quality and performance.</div>
          </transition>
        </li>
        <li>
          <a href="javascript:;" @click="changeBool('OSBool')">Our Service</a>
          <transition name="fade">
            <div v-show='boolList.OSBool'>Retail Solution/Wholesale Supply/Branding & Customization/Equipment Engineering/Custom Fitout</div>
          </transition>
        </li>
      </ul>
      <ul>
        <li>
          <a href="javascript:;" @click="changeBool('SHBool')">
            SERVICE HIGHLIGHT
          </a>
        </li>
        <li>
          <transition name="fade">
            <div v-show='boolList.SHBool'>
              <div>Feel like opening up a business or extending your catelogue?</div>
              <div>Our Melbourn based warehouse has over 1,000 types of products ready for your selection. Our fulfillment service team will also be able to get everything sorted for your business from packing to delivery.</div>
            </div>
          </transition>
        </li>
        <li>
          <a href="javascript:;" @click="changeBool('WSBool')">Wholesale Supply</a>
          <transition name="fade">
            <div v-show='boolList.WSBool'>
              <div>Competitive Pricing. No more middle man and back and forth nefotiation, you are speaking directly to your equipment manufacturer. Sourcing will become your very own competitive advantage.</div>
              <div>Seamless Connection. Communication with production will never be smoother, Your requirements are directly passed on to our production team without any distortion.</div>
            </div>
          </transition>
        </li>
        <li>
          <a href="javascript:;" @click="changeBool('CBANBool')">Custom Branding and Engineering</a>
          <transition name="fade">
            <div v-show='boolList.CBANBool'>
              <div>Trying to distinguish your business among the numerous rivals?</div>
              <div>We now offer custom branding and product engineering for your business. Simply tell us your thoughts and we will the most pratical advise based on years of experience with some top players in the industry.</div>
            </div>
          </transition>
        </li>
        <li>
          <a href="javascript:;" @click="changeBool('CFBool')">Custom Fitout</a>
          <transition name="fade">
            <div v-show='boolList.CFBool'>Send us a floor-plan of your desired gym space and will have everything sorted out for you. 30 years of production experiences with some of the world's sports retail giants, we have always act by one simple rule: it will work. And that's all it matters.</div>
          </transition>
        </li>
      </ul>
    </div>
    <div class="site">
      <ul class="QR-code">
        <li>
          <div>Contact Us</div>
          <div>admin@austarsports.com.au</div>
        </li>
        <li>
          <div>Showroom & Warehouse</div>
          <div>Unit 5/105 Cochranes Road, Moorabbin VIC 3189</div>
        </li>
        <li>
          <img class="QR-img" src="../../assets/QR.png" alt="">
        </li>
        <li>
          <a href="http://www.austarsports.com.au">http://www.austarsports.com.au</a>
        </li>
      </ul>
      <div class="icon">
        <a href="javascript:;"><i class="iconfont icon-Twitter"></i></a>
        <a href="javascript:;"><i class="iconfont icon-face-book"></i></a>
        <a href="javascript:;"><i class="iconfont icon-youtube"></i></a>
        <a href="javascript:;"><i class="iconfont icon-ins"></i></a>
      </div>
    </div>
    <div class="records">
      <a href="javascript:;" @click="changeLang">
        <img src="../../assets/au_sml.png" alt=""><
        <span class="country">Australia</span>
      </a>
      <span class="inc">© 2018 AUSTAR, INC. All Rights Reserved</span>
    </div>
  </div>
</template>
<script>
let WIDTH = document.body.clientWidth;
export default {
  name: '',
  data() {
    return {
      styleObj: {minWidth: `${WIDTH}px`},
      boolList: {
        AUBool: false,
        SHBool: false,
        SEBool: false,
        FBool: false,
        OBool: false,
        ABool: false,
        OPBBool: false,
        OPBool: false,
        OSBool: false,
        WSBool: false,
        CBANBool: false,
        CFBool: false
      }
    }
  },
  methods:{
    changeLang(){
      console.log("111");
      this.$router.push({name: 'language'});
    },
    changeBool(name){
      this.boolList[name] = !this.boolList[name];
    }
  }
}
</script>
<style scoped lang="scss">
  .footer{
    background-color: #000;
    padding: 20px 200px;
    color: #999;
    /* 动画 */
    .fade-enter-active, .fade-leave-active {
      transition: opacity .7s;
    }
    .fade-enter, .fade-leave-to{
      opacity: 0;
    }
    /* 动画结束 */
    .extra{
      display: flex;
      flex-wrap: wrap;
      ul{
        margin-right: 20px;
        flex: 1;
        li{
          font-size: .8em;
          margin-bottom: 5px;
          a{
            color: #ddd;
            font-weight: bold;
            &:hover{
              color: #fff;
            }
          }
          &:first-child{
            a{
              color: #fff;
            }
            font-size: 1em;
            font-weight: 400;
          }
        }
      }
    }
    .site{
      display: flex;
      justify-content: space-between;
      .QR-code{
        li{
          margin-bottom: 10px;
          font-size: 0.8em;
          text-align: center;
          .QR-img{
            width: 100px;
            height: 100px;
          }
          a{
            color: #eee;
          }
        }
      }
      .icon{
        align-self: flex-end;
        margin-bottom: 10px;
        i{
          font-size: 28px;
          color: #999;
          &:hover{
            color: #fff;
          }
        }
      }
    }
    .records{
      font-size: .625em;
      display: flex;
      justify-content: center;
      padding-top: 20px;
      border-top: 1px solid #ddd;
      img{
        width: 14px;
        height: 10px;
      }
      .country{
        color: #fff;
      }
      .inc{
        margin-left: 10px;
      }
    }
  }
</style>
