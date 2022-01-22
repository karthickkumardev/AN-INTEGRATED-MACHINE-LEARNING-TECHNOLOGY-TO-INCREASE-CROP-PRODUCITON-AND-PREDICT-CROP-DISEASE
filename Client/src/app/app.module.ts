import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IndexComponent } from './index/index.component';
import { CropProductionComponent } from './crop-production/crop-production.component';
import { CropDiseasePredictionComponent } from './crop-disease-prediction/crop-disease-prediction.component';

@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    CropProductionComponent,
    CropDiseasePredictionComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
