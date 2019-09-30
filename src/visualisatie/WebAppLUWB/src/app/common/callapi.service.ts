import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class CallapiService {

  constructor(private http: HttpClient) {}

  domain:string = "http://localhost:44308/api/";
  sortBy: string = "id";
  pageSize: number = 10;
  pageSizeDivider: number = 2;
  pageNumber:number = 1;
  public GetTags(){
    return this.http
    .get<TagAnchor[]>(`${this.domain}tags?sortBy=${this.sortBy}&pageSize=${this.pageSize/this.pageSizeDivider}&pageNumber=${this.pageNumber-1}`)
    .toPromise();
    //return this.http.get<TagAnchor[]>(`${this.domain}tags`);
  }
  public GetAnchors(){
    return this.http
    .get<TagAnchor[]>(`${this.domain}anchors?sortBy=${this.sortBy}&pageSize=${this.pageSize/this.pageSizeDivider}&pageNumber=${this.pageNumber-1}`)
    .toPromise();
    //return this.http.get<TagAnchor[]>(`${this.domain}anchors`);
  }
}

export interface TagAnchor {
  id: number;
  mac: string;
  description: string;
  xPos: number;
  yPos: number;
  type: string;
}