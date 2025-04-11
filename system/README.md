
Папка **system** создана для настройки инструментария сообщества
Пожалуйста не меняйте ее, если глубоко не понимаете что делаете. 


В разделе [Инструменты](system/tools/README.md) находящемся в папке **system/tools/** описаны программы которыми мы пользуемся.
* [Obsidian](system/tools/Obsidian.md)
* [Git](system/tools/Git.md)
* [GitHub](system/tools/GitHub.md)


# Обсидиан

Программа [Obsidian](system/tools/Obsidian.md) это записная книжка обладающая рядом свойств необходимых нашему сообществу. Она упрощает редактирование документации размещенной на [GitHub](system/tools/GitHub.md)

## Свойства

В разделе system/templates/ размещены шаблоны свойств для [Obsidian](system/tools/Obsidian.md) которые позволяют вставлять типовые наборы свойств в разные типы заметок: 
* [project](system/templates/project.md)
* [member](system/templates/member.md)
* [contract](system/templates/contract.md)

Свойства вставляемые шаблонами позволят автоматизировать обработку документации.

В разделе system/types/ размещены типы документов для [Obsidian](system/tools/Obsidian.md) тип документа надо заполнять в свойство типового документа для автоматизации. Зная тип документа в файле наши боты смогут знать какие свойства надо из него считать. 
Например: 
* [Договор](system/types/Contract.md)
* [Проект](system/types/Project.md)
* [Участник](system/types/Member.md)
