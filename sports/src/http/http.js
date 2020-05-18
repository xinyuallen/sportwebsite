import axios from 'axios';
let baseUrl = "http://202.195.167.248:80/market";

/*获取用户列表总数*/
export const getBrand = params => {
  return axios.get(`${baseUrl}/brand/`)
}

/*获取home大图*/
export const getHomePic = params => {
  return axios.get(`${baseUrl}/homePage/`)
}

/*获取category大图*/
export const getHomeCategory = params => {
  return axios.get(`${baseUrl}/homeCategory/`)
}

/*获取首页分类与子分类*/
export const getHomeSubCategory = params => {
  return axios.get(`${baseUrl}/subCategorys/`)
}

/*获取分类商品列表*/
export const getProductList = params => {
  return axios.get(`${baseUrl}/productsByCategory/`, {
    params: params
  })
}
