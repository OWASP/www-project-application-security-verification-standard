---

layout: col-sidebar
title: OWASP Application Security Verification Standard (ASVS)
tags: asvs
level: 4
type: standards
pitch: The OWASP Application Security Verification Standard (ASVS) Project is a framework of security requirements that focus on defining the security controls required when designing, developing and testing modern web applications and web services.
headerimage: ./assets/images/OWASP_ASVS_Linkedin_Banner-01.jpg
---
[![Creative Commons License](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/ "CC BY-SA 4.0")
[![OWASP Flagship](https://img.shields.io/badge/owasp-flagship%20project-48A646.svg)](https://www.owasp.org/index.php/Category:OWASP_Project#tab=Project_Inventory)
![Github stars ASVS](https://img.shields.io/github/stars/OWASP/asvs?label=Stars%20ASVS&style=social)
[![Twitter Follow](https://img.shields.io/twitter/follow/OWASP_ASVS.svg?style=social&label=Follow)](https://twitter.com/OWASP_ASVS)
[<img src="./assets/images/LinkedIn_Logo.svg" height=20>](https://www.linkedin.com/company/owasp-asvs/)

## What is the ASVS?

The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.

## Support the ASVS

For more details on how to financially support the ASVS, see our [Supporters Page](https://appsecg.host/fundasvs).

## Stay up to date with the ASVS

Follow us on social media to ensure you don't miss updates about the ASVS:
* [![Twitter Follow](https://img.shields.io/twitter/follow/OWASP_ASVS.svg?style=social&label=Follow)](https://twitter.com/OWASP_ASVS)
* [<img src="./assets/images/LinkedIn_Logo.svg" height=20>](https://www.linkedin.com/company/owasp-asvs/)

## More Details on the ASVS

The primary aim of the **OWASP Application Security Verification Standard (ASVS) Project** is to normalize the range in the coverage and level of rigor available in the market when it comes to performing Web application security verification using a commercially-workable open standard. The standard provides a basis for testing application technical security controls, as well as any technical security controls in the environment, that are relied on to protect against vulnerabilities such as Cross-Site Scripting (XSS) and SQL injection. This standard can be used to establish a level of confidence in the security of Web applications. The requirements were developed with the following objectives in mind: 

* **Use as a metric** - Provide application developers and application owners with a yardstick with which to assess the degree of trust that can be placed in their Web applications, 
* **Use as guidance** - Provide guidance to security control developers as to what to build into security controls in order to satisfy application security requirements, and 
* **Use during procurement** - Provide a basis for specifying application security verification requirements in contracts.

Get the latest stable version of the ASVS (5.0.0) from the [Downloads](https://github.com/OWASP/ASVS/tree/v5.0.0#latest-stable-version---500) page.

## How To Reference ASVS Requirements

Each requirement has an identifier in the format `<chapter>.<section>.<requirement>`, where each element is a number. For example, `1.11.3`.

* The `<chapter>` value corresponds to the chapter from which the requirement comes; for example, all `1.#.#` requirements are from the 'Encoding and Sanitization' chapter.
* The `<section>` value corresponds to the section within that chapter where the requirement appears, for example: all `1.2.#` requirements are in the 'Injection Prevention' section of the 'Encoding and Sanitization' chapter.
* The `<requirement>` value identifies the specific requirement within the chapter and section, for example, `1.2.5` which as of version 5.0.0 of this standard is:

> Verify that the application protects against OS command injection and that operating system calls use parameterized OS queries or use contextual command line output encoding.

Since the identifiers may change between versions of the standard, it is preferable for other documents, reports, or tools to use the following format: `v<version>-<chapter>.<section>.<requirement>`, where: 'version' is the ASVS version tag. For example: `v5.0.0-1.2.5` would be understood to mean specifically the 5th requirement in the 'Injection Prevention' section of the 'Encoding and Sanitization' chapter from version 5.0.0. (This could be summarized as `v<version>-<requirement_identifier>`.)

Note: The `v` preceding the version number in the format should always be lowercase.

If identifiers are used without including the `v<version>` element then they should be assumed to refer to the latest Application Security Verification Standard content. As the standard grows and changes this becomes problematic, which is why writers or developers should include the version element.

ASVS requirement lists are made available in [CSV, JSON, and other formats](https://github.com/OWASP/ASVS) which may be useful for reference or programmatic use.

## Related Projects

OWASP Resources:
* [OWASP Top Ten Proactive Controls (2018)](https://top10proactive.owasp.org/)
* [OWASP Top Ten Risks (2017)](https://owasp.org/Top10/)
* [OWASP Cheatsheet Series](https://cheatsheetseries.owasp.org/index.html)
