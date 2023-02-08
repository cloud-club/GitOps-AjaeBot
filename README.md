# Git깔 나는 Ops


Cloub Club 2기 시즌2  **Git깔 나는 Ops** 팀의 CI/CD 파이프라인 구축기

- [프로젝트 진행 노션](https://www.notion.so/cloudclub/Git-Ops-c669d76dfbfe4cc781a2be58e599623d)
- [최종 발표 영상](https://youtu.be/PoSEdVg2cFQ)

## 프로젝트 소개 👋


두개의 팀으로 나누어 간단한 slack bot 을 생성하고 , GitOps 방식의 CI/CD 구축하기!

### 아재봇

> 클둥이들이 피식할 수 있는 아재개그를 알려주는 슬랙봇

- 팀원: 주영, 해송
- Application Repo: [AjaeBot](https://github.com/cloud-club/GitOps-AjaeBot)
- Config Repo: [AjaeBot-Config](https://github.com/cloud-club/GitOps-AjaeBot-Config)

### 생일봇

> 클둥이들의 생일을 축하해주는 슬랙봇

- 팀원: 유경, 지우, 채희
- Application Repo: [ChucarBot](https://github.com/cloud-club/GitOps-ChucarBot)
- Config Repo: [ChucarBot-Manifest](https://github.com/cloud-club/GitOps-ChucarBot-Manifest)

## 팀원 소개 🥇

### TL
- [박진희](https://github.com/gineepark)
### 아재봇 개발 & CI/CD
- [김주영](https://github.com/juyoung810)
- [이해송](https://github.com/pinetree2)
### 생일봇 개발 & CI/CD
- [강채희](https://github.com/chaeheekang)
- [정지우](https://github.com/ziwooda)
- [현유경](https://github.com/yugyeongh)

## 프로젝트 아키텍처⚙️

![프로젝트 아키텍처](https://user-images.githubusercontent.com/57140735/217547435-2c75a736-5223-4fa3-9f97-9f3cc33c27de.png)

- 아재봇 팀은 `Deployment` 를 생성해 쿠버네티스 환경에서 애플리케이션을 관리, `helm chart` 를 만들어 쿠버네티스 환경에 배포
- 생일봇 팀은 자정마다 애플리케이션이 실행될 수 있도록 `Cronjob` 을 생성해 애플리케이션을 관리

## 팀 별 시연 🔍
| 아재봇 | 생일봇|
| ---- | ----|
|<img src="https://user-images.githubusercontent.com/57140735/217547699-797baa9c-65cc-4b63-ab22-1d0af63e9817.gif" width="500px" height="300px" >|<img width="500px" height="300px" alt="image" src="https://user-images.githubusercontent.com/57140735/217550837-286a2440-ed84-4a14-978e-52a89e1bcdad.png">|

## 프로젝트 타임라인 ✔️

<p align="center">
<img src="https://user-images.githubusercontent.com/57140735/217548014-b5efebbc-a29c-4616-bb4c-0096f391ddd3.png" width="300px" height="400px" >
<img src="https://user-images.githubusercontent.com/57140735/217548084-7d4937cc-c6e9-4fb5-9285-57d3d6bd4a8a.png" width="300px" height="400px" >
</p>
