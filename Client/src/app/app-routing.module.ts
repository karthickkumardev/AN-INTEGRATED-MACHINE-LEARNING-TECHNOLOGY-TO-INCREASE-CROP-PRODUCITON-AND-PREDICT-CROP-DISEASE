import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CropDiseasePredictionComponent } from './crop-disease-prediction/crop-disease-prediction.component';
import { CropProductionComponent } from './crop-production/crop-production.component';
import { IndexComponent } from './index/index.component';

const routes: Routes = [
  
  {
    path:'',
    redirectTo:'index',
    pathMatch:'full'
  },
  {
    path:'index',
    component:IndexComponent
  },
  {
    path:'crop-production',
    component:CropProductionComponent
  },
  {
    path:'crop-disease-prediciton',
    component:CropDiseasePredictionComponent
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
