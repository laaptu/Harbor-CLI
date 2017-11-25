# Change Log

## [v1.0.0](https://github.com/srishanbhattarai/Harbor-CLI/tree/v1.0.0) (2017-11-22)
**Implemented enhancements:**

- Add support for Python 3.3 [\#43](https://github.com/srishanbhattarai/Harbor-CLI/issues/43)
- Add a script `t` for automating manual tasks. [\#33](https://github.com/srishanbhattarai/Harbor-CLI/pull/33) ([kabirbaidhya](https://github.com/kabirbaidhya))

**Closed issues:**

- Evaluate compatibility with Python 3.1, 3.2 [\#45](https://github.com/srishanbhattarai/Harbor-CLI/issues/45)
- Better strategy for icon discovery [\#26](https://github.com/srishanbhattarai/Harbor-CLI/issues/26)
- Versioning support. [\#25](https://github.com/srishanbhattarai/Harbor-CLI/issues/25)
- gradle clean before build [\#24](https://github.com/srishanbhattarai/Harbor-CLI/issues/24)
- HipChat config KeyError checks [\#23](https://github.com/srishanbhattarai/Harbor-CLI/issues/23)
- Add checks to make sure project exists whenever an invitation is sent [\#7](https://github.com/srishanbhattarai/Harbor-CLI/issues/7)
- Decouple project name getters from deploy/registration services [\#6](https://github.com/srishanbhattarai/Harbor-CLI/issues/6)
- Delay storage  upload in the  delegate until sanity  checks are done [\#4](https://github.com/srishanbhattarai/Harbor-CLI/issues/4)
- Missing fail safes for duplicate registration of projects. [\#3](https://github.com/srishanbhattarai/Harbor-CLI/issues/3)

**Merged pull requests:**

- HB-38: Flag to say yes to everything during deployment. [\#48](https://github.com/srishanbhattarai/Harbor-CLI/pull/48) ([srishanbhattarai](https://github.com/srishanbhattarai))
- \(chore\) Add pytest and pylint to setup.py extras\_require [\#47](https://github.com/srishanbhattarai/Harbor-CLI/pull/47) ([mesaugat](https://github.com/mesaugat))
- Fix \#43 Add Python3.3 support [\#44](https://github.com/srishanbhattarai/Harbor-CLI/pull/44) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Fix \#23 HipChat key checks [\#37](https://github.com/srishanbhattarai/Harbor-CLI/pull/37) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Refactor registration service [\#36](https://github.com/srishanbhattarai/Harbor-CLI/pull/36) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Refactor invitation service. [\#35](https://github.com/srishanbhattarai/Harbor-CLI/pull/35) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Add --version CLI option to show the version [\#34](https://github.com/srishanbhattarai/Harbor-CLI/pull/34) ([kabirbaidhya](https://github.com/kabirbaidhya))
- Refactor deployment services [\#32](https://github.com/srishanbhattarai/Harbor-CLI/pull/32) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Refactor codebase. [\#31](https://github.com/srishanbhattarai/Harbor-CLI/pull/31) ([srishanbhattarai](https://github.com/srishanbhattarai))
- \(fix\) added install requires and changes [\#30](https://github.com/srishanbhattarai/Harbor-CLI/pull/30) ([ypradhan](https://github.com/ypradhan))
- \(chore\) Fix README.md typo and changed description. [\#29](https://github.com/srishanbhattarai/Harbor-CLI/pull/29) ([ypradhan](https://github.com/ypradhan))
- Create CODE\_OF\_CONDUCT.md [\#28](https://github.com/srishanbhattarai/Harbor-CLI/pull/28) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Setup travis CI [\#27](https://github.com/srishanbhattarai/Harbor-CLI/pull/27) ([srishanbhattarai](https://github.com/srishanbhattarai))
- HipChat support [\#22](https://github.com/srishanbhattarai/Harbor-CLI/pull/22) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Changelog support [\#21](https://github.com/srishanbhattarai/Harbor-CLI/pull/21) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Refactor codebase [\#20](https://github.com/srishanbhattarai/Harbor-CLI/pull/20) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Issue-7: Add check for non-existent project during invitation [\#17](https://github.com/srishanbhattarai/Harbor-CLI/pull/17) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Issue-6 Decouple project name getter from deployment service [\#16](https://github.com/srishanbhattarai/Harbor-CLI/pull/16) ([srishanbhattarai](https://github.com/srishanbhattarai))
- v2-deploy: Migrate deployment services [\#15](https://github.com/srishanbhattarai/Harbor-CLI/pull/15) ([srishanbhattarai](https://github.com/srishanbhattarai))
- A util to destructure dictonaries [\#14](https://github.com/srishanbhattarai/Harbor-CLI/pull/14) ([srishanbhattarai](https://github.com/srishanbhattarai))
- \(v2, migrate\) Migrate invitation service to v2 architecture [\#13](https://github.com/srishanbhattarai/Harbor-CLI/pull/13) ([srishanbhattarai](https://github.com/srishanbhattarai))
- v2: Migration to a plugin architecture [\#11](https://github.com/srishanbhattarai/Harbor-CLI/pull/11) ([srishanbhattarai](https://github.com/srishanbhattarai))
- FCM trigger cloud functions [\#10](https://github.com/srishanbhattarai/Harbor-CLI/pull/10) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Invitation service. [\#8](https://github.com/srishanbhattarai/Harbor-CLI/pull/8) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Upload project under a release type which is configured via a CLI flag [\#5](https://github.com/srishanbhattarai/Harbor-CLI/pull/5) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Firebase functions and cascade database entry upon registration [\#2](https://github.com/srishanbhattarai/Harbor-CLI/pull/2) ([srishanbhattarai](https://github.com/srishanbhattarai))
- Registration Services [\#1](https://github.com/srishanbhattarai/Harbor-CLI/pull/1) ([srishanbhattarai](https://github.com/srishanbhattarai))



\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*
