--DROP TABLE [dbo].[__EFMigrationsHistory];
--DROP TABLE [dbo].[Anchors];
--DROP TABLE [dbo].[Demos];
--ALTER TABLE [dbo].[Anchors] DROP CONSTRAINT [FK_Anchors_Maps_MapId];
--ALTER TABLE [dbo].[Tags] DROP CONSTRAINT [FK_Tags_Maps_MapId];
--DROP TABLE [dbo].[Maps];
--DROP TABLE [dbo].[Measurements];
--DROP TABLE [dbo].[Tags];
--ALTER TABLE [dbo].[Anchors] DROP CONSTRAINT [FK_Anchors_Users_UserId];
--ALTER TABLE [dbo].[Maps] DROP CONSTRAINT [FK_Maps_Users_UserId];
--ALTER TABLE [dbo].[Tags] DROP CONSTRAINT [FK_Tags_Users_UserId];
--DROP TABLE [dbo].[Users];
DROP TABLE [HangFire].[AggregatedCounter];
DROP TABLE [HangFire].[Counter];
DROP TABLE [HangFire].[Hash];
ALTER TABLE [HangFire].[JobParameter] DROP CONSTRAINT [FK_HangFire_JobParameter_Job];
ALTER TABLE [HangFire].[State] DROP CONSTRAINT [FK_HangFire_State_Job];
DROP TABLE [HangFire].[Job];
DROP TABLE [HangFire].[JobParameter];
DROP TABLE [HangFire].[JobQueue];
DROP TABLE [HangFire].[List];
DROP TABLE [HangFire].[Schema];
DROP TABLE [HangFire].[Server];
DROP TABLE [HangFire].[Set];
DROP TABLE [HangFire].[State];

