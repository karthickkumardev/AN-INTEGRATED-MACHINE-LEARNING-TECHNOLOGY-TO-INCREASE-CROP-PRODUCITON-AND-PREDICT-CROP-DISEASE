import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CropProductionComponent } from './crop-production/crop-production.component';
import { IndexComponent } from './index/index.component';

const routes: Routes = [
  
  {
    path:'/',
    component:IndexComponent
  },
  {
    path:'/index',
    component:IndexComponent
  },
  {
    path:'/crop-production',
    component:CropProductionComponent
  },
  {
    path:'/crop-disease-prediciton',
    component:CropProductionComponent
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
