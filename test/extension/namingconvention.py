#!/usr/bin/env python3

import yaz


class ThisWasCamelCase(yaz.Plugin):
    @yaz.task
    def this_was_underscored(self):
        return "this-was-underscored"

    @yaz.task
    def thisWasCamelCase(self):
        return "this-was-camel-case"

    @yaz.task
    def _this___was_also__underscored___(self):
        return "this-was-also-underscored"


if __name__ == "__main__":
    yaz.main()
