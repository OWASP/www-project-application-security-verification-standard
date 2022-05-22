---

layout: col-sidebar
title: OWASP Application Security Verification Standard
tags: asvs
level: 4
type: standards
pitch: The OWASP Application Security Verification Standard (ASVS) Project is a framework of security requirements that focus on defining the security controls required when designing, developing and testing modern web applications and web services.

---
[![Creative Commons License](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/ "CC BY-SA 4.0")
[![OWASP Flagship](https://img.shields.io/badge/owasp-flagship%20project-48A646.svg)](https://www.owasp.org/index.php/Category:OWASP_Project#tab=Project_Inventory)
![Github stars ASVS](https://img.shields.io/github/stars/OWASP/asvs?label=Stars%20ASVS&style=social)
[![Twitter Follow](https://img.shields.io/twitter/follow/OWASP_ASVS.svg?style=social&label=Follow)](https://twitter.com/OWASP_ASVS)

## What is the ASVS?

The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.

The primary aim of the **OWASP Application Security Verification Standard (ASVS) Project** is to normalize the range in the coverage and level of rigor available in the market when it comes to performing Web application security verification using a commercially-workable open standard. The standard provides a basis for testing application technical security controls, as well as any technical security controls in the environment, that are relied on to protect against vulnerabilities such as Cross-Site Scripting (XSS) and SQL injection. This standard can be used to establish a level of confidence in the security of Web applications. The requirements were developed with the following objectives in mind: 

* **Use as a metric** - Provide application developers and application owners with a yardstick with which to assess the degree of trust that can be placed in their Web applications, 
* **Use as guidance** - Provide guidance to security control developers as to what to build into security controls in order to satisfy application security requirements, and 
* **Use during procurement** - Provide a basis for specifying application security verification requirements in contracts.

Get the latest stable version of the ASVS (4.0.3) from the [Downloads](https://github.com/OWASP/ASVS/tree/v4.0.3#latest-stable-version---403) page and **the [plan and roadmap](https://owasp.org/blog/2022/05/15/asvs-5.0-roadmap.html) towards ASVS version 5.0 has been announced!**

## How To Reference ASVS Requirements

Each requirement has an identifier in the format `<chapter>.<section>.<requirement>` where each element is a number, for example: `1.11.3`.
- The `<chapter>` value corresponds to the chapter from which the requirement comes, for example: all `1.#.#` requirements are from the `Architecture` chapter.
- The `<section>` value corresponds to the section within that chapter where the requirement appears, for example: all `1.11.#` requirements are in the `Business Logic Architecture` section of the `Architecture` chapter.
- The `<requirement>` value identifies the specific requirement within the chapter and section, for example: `1.11.3` which as of version 4.0.3 of this standard is:

> Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions.

The identifiers may change between versions of the standard therefore it is preferable that other documents, reports, or tools use the format: `v<version>-<chapter>.<section>.<requirement>`, where: 'version' is the ASVS version tag. For example: `v4.0.3-1.11.3` would be understood to mean specifically the 3rd requirement in the 'Business Logic Architecture' section of the 'Architecture' chapter from version 4.0.3. (This could be summarized as `v<version>-<requirement_identifier>`.)

Note: The `v` preceding the version portion is to be lower case.

If identifiers are used without including the `v<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. Obviously as the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

ASVS requirement lists are made available in [CSV, JSON, and other formats](https://github.com/OWASP/ASVS) which may be useful for reference or programmatic use.

## Related Projects

OWASP Resources:
* [OWASP Top Ten Proactive Controls (2018)](https://www.owasp.org/index.php/OWASP_Proactive_Controls)
* [OWASP Top Ten Risks (2017)](http://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)
* [OWASP Cheatsheet Series](https://www.owasp.org/index.php/OWASP_Cheat_Sheet_Series)
