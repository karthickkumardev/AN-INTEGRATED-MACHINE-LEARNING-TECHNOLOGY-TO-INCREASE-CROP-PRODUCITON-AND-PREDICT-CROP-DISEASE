import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CropDiseasePredictionComponent } from './crop-disease-prediction.component';

describe('CropDiseasePredictionComponent', () => {
  let component: CropDiseasePredictionComponent;
  let fixture: ComponentFixture<CropDiseasePredictionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CropDiseasePredictionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CropDiseasePredictionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
