# Diccionario de utters, lo usaremos para identificar qué audio hay que enviar en función del idioma y el texto

diccionario_utters = {
    "ES": {
        """Hola de nuevo. ¿En qué puedo ayudarte esta vez?"""
        : "utter_saludo",

        "Ha sido un placer poder acompañarte. No olvides que, si me necesitas otra vez, estaré disponible para ti en cualquier momento. ¡Por cierto! No dudes en hablarle de mí a otras personas que puedan haber pasado o estén pasando por una situación similar. Contarlo y actuar puede cambiar mucho las cosas."
        : "utter_despedida",

        "Soy un bot, hecho con Rasa. Mi propósito es acompañar a personas que han podido ser víctimas de delitos de odio, ofreciéndoles un espacio seguro donde poder contar lo sucedido y poniendo a su alcance diferentes recursos dependiendo de sus necesidades"
        : "utter_soydelia",

        """Hablar de ello es el primer paso para que se haga justicia. Durante este proceso te haré algunas preguntas personales para crear un informe detallado y ayudarte a entender si lo que has vivido se trata de un delito de odio.
      Es importante tener en cuenta que cuanta más información me des, más fácil será poder ayudarte, pero no tienes por qué contestar a todo.
      Tu espacio y tu seguridad son lo más importante, por eso, esta conversación no quedará registrada en ningún lado.
      ¿Quieres que empecemos el cuestionario? Solo te llevará X minutos."""
        : "utter_testimonio",

        """Entiendo, y está bien decir que no. Solo por si acaso, quiero que sepas que puede ser la forma de recibir un acompañamiento más ajustado a lo que necesitas, sin juzgarte y siempre con total confidencialidad. Tú decides el ritmo, ¿te animas a intentarlo?"""
        : "utter_pedir_confirmacion",

        """De acuerdo, podemos hablar en otro momento. Aun así, recuerda de que todas las personas merecen ser respetadas tal y como son.
       ¡Y, por cierto! No dudes en hablarle de mí a otras personas que puedan haber pasado o estén pasando por una situación similar. Contarlo y actuar puede cambiar mucho las cosas. Estoy aquí siempre que me necesites."""
        : "utter_despedida_concienciadora",

        """Genial, antes de que me cuentes lo que ha pasado necesito conocerte mejor. ¿Podrías decirme tu nombre, edad, género y nacionalidad?"""
        : "utter_inform_perfil_victima1",

        """Gracias por la información. Entender con qué grupo social te identificas puede ayudarme a comprender mejor lo que pasó.
       ¿Te reconoces como LGTBIQ+, formas parte de una comunidad religiosa o de algún otro colectivo que sea importante para ti?"""
        : "utter_inform_perfil_victima2_v1",

        """Gracias por la información. ¿Te sientes parte de alguna comunidad, etnia o grupo, como por ejemplo LGTBIQ+, una comunidad religiosa u otro colectivo que pueda ser importante para lo sucedido? Esto me puede ayudar a entender mejor tu situación."""
        : "utter_inform_perfil_victima2_v2",

        """¿El incidente sucedió a través de internet o en un lugar físico?"""
        : "utter_ubicar_medio",

        """¿Podrías decirme en qué red o redes ocurrieron los hechos?"""
        : "utter_plataforma_redes_v1",

        """¿En qué redes sociales tuvo lugar lo sucedido?"""
        : "utter_plataforma_redes_v2",

        """¿A través de qué espacio digital sucedió el incidente?"""
        : "utter_plataforma_redes_v3",

        """¿Cuándo ocurrió lo sucedido? Puede ser una fecha y hora específicos o un período aproximado."""
        : "utter_fecha_redes_v1",

        """¿En qué fecha o período tuvo lugar lo que pasó en redes? Si no lo recuerdas bien puedes darme datos aproximados."""
        : "utter_fecha_redes_v2",

        """¿Fueron una o varias las cuentas que participaron en lo sucedido?"""
        : "utter_num_agresores_redes",

        """¿Recuerdas el nombre de usuario, correo o perfil del agresor en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: ¿sabías si esta cuenta seguía o estaba vinculada a grupos o páginas con ideologías de odio o compartía contenido de odio?"""
        : "utter_pregunta_cuenta_agresor_vinculacion_redes_v1",

        """¿Recuerdas el nombre de usuario, correo o perfil del agresor en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: a veces los perfiles comparten contenido o usan imágenes de perfil o nombres relacionados con grupos extremistas. ¿Viste algo así?"""
        : "utter_pregunta_cuenta_agresor_vinculacion_redes_v2",

        """¿Recuerdas los nombres de usuario, correos o perfiles de los agresores en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: ¿sabías si estas cuentas seguían o estaban vinculadas a grupos o páginas con ideologías de odio o compartían contenido de odio?"""
        : "utter_pregunta_cuenta_agresores_vinculacion_redes_v1",

        """¿Recuerdas los nombres de usuario, correos o perfiles de los agresores en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: a veces los perfiles comparten contenido o usan imágenes de perfil o nombres relacionados con grupos extremistas. ¿Viste algo así?"""
        : "utter_pregunta_cuenta_agresores_vinculacion_redes_v2",

        """Cuando quieras puedes empezar a contarme lo que te ha pasado. Para que todo sea más fácil, trata de seguir el orden en que ocurrió el incidente y, si puedes, reproduce mensajes o imágenes tal como las recuerdas."""
        : "utter_invita_relato_hechos_v1",

        """Este es un espacio seguro. Puedes contar todo lo que recuerdes sobre el incidente. Será todo más fácil si me lo cuentas en orden, incluyendo los mensajes o publicaciones, y describiendo cualquier contenido que te parezca relevante."""
        : "utter_invita_relato_hechos_v2",

        """Gracias por compartir todo esto conmigo. Si hay algo más que recuerdes y te gustaría añadir, puedes hacerlo ahora. Antes de que continuemos, me gustaría hacerte una pregunta más. ¿Crees que hubo algún motivo detrás de la agresión o el comportamiento de esa persona?"""
        : "utter_invita_relato_adicional_motivacion_v1",

        """Lo que has contado hasta ahora es importante. Si sientes que quedó algo fuera o recuerdas algún otro detalle, puedes compartirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que el agresor actuó así?"""
        : "utter_invita_relato_adicional_motivacion_v2",

        """Agradezco que hayas compartido tu relato. Si se te ocurre algo más que quieras contar, puedes añadirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que el agresor actuó así?"""
        : "utter_invita_relato_adicional_motivacion_v3",

        """Gracias por compartir todo esto conmigo. Si hay algo más que recuerdes y te gustaría añadir, puedes hacerlo ahora. Antes de que continuemos, me gustaría hacerte una pregunta más. ¿Crees que hubo algún motivo detrás de la agresión o el comportamiento de esas personas?"""
        : "utter_invita_relato_adicional_motivacion_plural_v1",

        """Lo que has contado hasta ahora es importante. Si sientes que quedó algo fuera o recuerdas algún otro detalle, puedes compartirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que los agresores actuaron así?"""
        : "utter_invita_relato_adicional_motivacion_plural_v2",

        """Agradezco que hayas compartido tu relato. Si se te ocurre algo más que quieras contar, puedes añadirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que los agresores actuaron así?"""
        : "utter_invita_relato_adicional_motivacion_plural_v3"
    },
    "EN": {
        """Hola de nuevo. ¿En qué puedo ayudarte esta vez?"""
        : "utter_saludo",

        "Ha sido un placer poder acompañarte. No olvides que, si me necesitas otra vez, estaré disponible para ti en cualquier momento. ¡Por cierto! No dudes en hablarle de mí a otras personas que puedan haber pasado o estén pasando por una situación similar. Contarlo y actuar puede cambiar mucho las cosas."
        : "utter_despedida",

        "Soy un bot, hecho con Rasa. Mi propósito es acompañar a personas que han podido ser víctimas de delitos de odio, ofreciéndoles un espacio seguro donde poder contar lo sucedido y poniendo a su alcance diferentes recursos dependiendo de sus necesidades"
        : "utter_soydelia",

        """Hablar de ello es el primer paso para que se haga justicia. Durante este proceso te haré algunas preguntas personales para crear un informe detallado y ayudarte a entender si lo que has vivido se trata de un delito de odio.
      Es importante tener en cuenta que cuanta más información me des, más fácil será poder ayudarte, pero no tienes por qué contestar a todo.
      Tu espacio y tu seguridad son lo más importante, por eso, esta conversación no quedará registrada en ningún lado.
      ¿Quieres que empecemos el cuestionario? Solo te llevará X minutos."""
        : "utter_testimonio",

        """Entiendo, y está bien decir que no. Solo por si acaso, quiero que sepas que puede ser la forma de recibir un acompañamiento más ajustado a lo que necesitas, sin juzgarte y siempre con total confidencialidad. Tú decides el ritmo, ¿te animas a intentarlo?"""
        : "utter_pedir_confirmacion",

        """De acuerdo, podemos hablar en otro momento. Aun así, recuerda de que todas las personas merecen ser respetadas tal y como son.
       ¡Y, por cierto! No dudes en hablarle de mí a otras personas que puedan haber pasado o estén pasando por una situación similar. Contarlo y actuar puede cambiar mucho las cosas. Estoy aquí siempre que me necesites."""
        : "utter_despedida_concienciadora",

        """Genial, antes de que me cuentes lo que ha pasado necesito conocerte mejor. ¿Podrías decirme tu nombre, edad, género y nacionalidad?"""
        : "utter_inform_perfil_victima1",

        """Gracias por la información. Entender con qué grupo social te identificas puede ayudarme a comprender mejor lo que pasó.
       ¿Te reconoces como LGTBIQ+, formas parte de una comunidad religiosa o de algún otro colectivo que sea importante para ti?"""
        : "utter_inform_perfil_victima2_v1",

        """Gracias por la información. ¿Te sientes parte de alguna comunidad, etnia o grupo, como por ejemplo LGTBIQ+, una comunidad religiosa u otro colectivo que pueda ser importante para lo sucedido? Esto me puede ayudar a entender mejor tu situación."""
        : "utter_inform_perfil_victima2_v2",

        """¿El incidente sucedió a través de internet o en un lugar físico?"""
        : "utter_ubicar_medio",

        """¿Podrías decirme en qué red o redes ocurrieron los hechos?"""
        : "utter_plataforma_redes_v1",

        """¿En qué redes sociales tuvo lugar lo sucedido?"""
        : "utter_plataforma_redes_v2",

        """¿A través de qué espacio digital sucedió el incidente?"""
        : "utter_plataforma_redes_v3",

        """¿Cuándo ocurrió lo sucedido? Puede ser una fecha y hora específicos o un período aproximado."""
        : "utter_fecha_redes_v1",

        """¿En qué fecha o período tuvo lugar lo que pasó en redes? Si no lo recuerdas bien puedes darme datos aproximados."""
        : "utter_fecha_redes_v2",

        """¿Fueron una o varias las cuentas que participaron en lo sucedido?"""
        : "utter_num_agresores_redes",

        """¿Recuerdas el nombre de usuario, correo o perfil del agresor en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: ¿sabías si esta cuenta seguía o estaba vinculada a grupos o páginas con ideologías de odio o compartía contenido de odio?"""
        : "utter_pregunta_cuenta_agresor_vinculacion_redes_v1",

        """¿Recuerdas el nombre de usuario, correo o perfil del agresor en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: a veces los perfiles comparten contenido o usan imágenes de perfil o nombres relacionados con grupos extremistas. ¿Viste algo así?"""
        : "utter_pregunta_cuenta_agresor_vinculacion_redes_v2",

        """¿Recuerdas los nombres de usuario, correos o perfiles de los agresores en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: ¿sabías si estas cuentas seguían o estaban vinculadas a grupos o páginas con ideologías de odio o compartían contenido de odio?"""
        : "utter_pregunta_cuenta_agresores_vinculacion_redes_v1",

        """¿Recuerdas los nombres de usuario, correos o perfiles de los agresores en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: a veces los perfiles comparten contenido o usan imágenes de perfil o nombres relacionados con grupos extremistas. ¿Viste algo así?"""
        : "utter_pregunta_cuenta_agresores_vinculacion_redes_v2",

        """Cuando quieras puedes empezar a contarme lo que te ha pasado. Para que todo sea más fácil, trata de seguir el orden en que ocurrió el incidente y, si puedes, reproduce mensajes o imágenes tal como las recuerdas."""
        : "utter_invita_relato_hechos_v1",

        """Este es un espacio seguro. Puedes contar todo lo que recuerdes sobre el incidente. Será todo más fácil si me lo cuentas en orden, incluyendo los mensajes o publicaciones, y describiendo cualquier contenido que te parezca relevante."""
        : "utter_invita_relato_hechos_v2",

        """Gracias por compartir todo esto conmigo. Si hay algo más que recuerdes y te gustaría añadir, puedes hacerlo ahora. Antes de que continuemos, me gustaría hacerte una pregunta más. ¿Crees que hubo algún motivo detrás de la agresión o el comportamiento de esa persona?"""
        : "utter_invita_relato_adicional_motivacion_v1",

        """Lo que has contado hasta ahora es importante. Si sientes que quedó algo fuera o recuerdas algún otro detalle, puedes compartirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que el agresor actuó así?"""
        : "utter_invita_relato_adicional_motivacion_v2",

        """Agradezco que hayas compartido tu relato. Si se te ocurre algo más que quieras contar, puedes añadirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que el agresor actuó así?"""
        : "utter_invita_relato_adicional_motivacion_v3",

        """Gracias por compartir todo esto conmigo. Si hay algo más que recuerdes y te gustaría añadir, puedes hacerlo ahora. Antes de que continuemos, me gustaría hacerte una pregunta más. ¿Crees que hubo algún motivo detrás de la agresión o el comportamiento de esas personas?"""
        : "utter_invita_relato_adicional_motivacion_plural_v1",

        """Lo que has contado hasta ahora es importante. Si sientes que quedó algo fuera o recuerdas algún otro detalle, puedes compartirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que los agresores actuaron así?"""
        : "utter_invita_relato_adicional_motivacion_plural_v2",

        """Agradezco que hayas compartido tu relato. Si se te ocurre algo más que quieras contar, puedes añadirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que los agresores actuaron así?"""
        : "utter_invita_relato_adicional_motivacion_plural_v3"
    },
    "FR": {
        """Hola de nuevo. ¿En qué puedo ayudarte esta vez?"""
        : "utter_saludo",

        "Ha sido un placer poder acompañarte. No olvides que, si me necesitas otra vez, estaré disponible para ti en cualquier momento. ¡Por cierto! No dudes en hablarle de mí a otras personas que puedan haber pasado o estén pasando por una situación similar. Contarlo y actuar puede cambiar mucho las cosas."
        : "utter_despedida",

        "Soy un bot, hecho con Rasa. Mi propósito es acompañar a personas que han podido ser víctimas de delitos de odio, ofreciéndoles un espacio seguro donde poder contar lo sucedido y poniendo a su alcance diferentes recursos dependiendo de sus necesidades"
        : "utter_soydelia",

        """Hablar de ello es el primer paso para que se haga justicia. Durante este proceso te haré algunas preguntas personales para crear un informe detallado y ayudarte a entender si lo que has vivido se trata de un delito de odio.
      Es importante tener en cuenta que cuanta más información me des, más fácil será poder ayudarte, pero no tienes por qué contestar a todo.
      Tu espacio y tu seguridad son lo más importante, por eso, esta conversación no quedará registrada en ningún lado.
      ¿Quieres que empecemos el cuestionario? Solo te llevará X minutos."""
        : "utter_testimonio",

        """Entiendo, y está bien decir que no. Solo por si acaso, quiero que sepas que puede ser la forma de recibir un acompañamiento más ajustado a lo que necesitas, sin juzgarte y siempre con total confidencialidad. Tú decides el ritmo, ¿te animas a intentarlo?"""
        : "utter_pedir_confirmacion",

        """De acuerdo, podemos hablar en otro momento. Aun así, recuerda de que todas las personas merecen ser respetadas tal y como son.
       ¡Y, por cierto! No dudes en hablarle de mí a otras personas que puedan haber pasado o estén pasando por una situación similar. Contarlo y actuar puede cambiar mucho las cosas. Estoy aquí siempre que me necesites."""
        : "utter_despedida_concienciadora",

        """Genial, antes de que me cuentes lo que ha pasado necesito conocerte mejor. ¿Podrías decirme tu nombre, edad, género y nacionalidad?"""
        : "utter_inform_perfil_victima1",

        """Gracias por la información. Entender con qué grupo social te identificas puede ayudarme a comprender mejor lo que pasó.
       ¿Te reconoces como LGTBIQ+, formas parte de una comunidad religiosa o de algún otro colectivo que sea importante para ti?"""
        : "utter_inform_perfil_victima2_v1",

        """Gracias por la información. ¿Te sientes parte de alguna comunidad, etnia o grupo, como por ejemplo LGTBIQ+, una comunidad religiosa u otro colectivo que pueda ser importante para lo sucedido? Esto me puede ayudar a entender mejor tu situación."""
        : "utter_inform_perfil_victima2_v2",

        """¿El incidente sucedió a través de internet o en un lugar físico?"""
        : "utter_ubicar_medio",

        """¿Podrías decirme en qué red o redes ocurrieron los hechos?"""
        : "utter_plataforma_redes_v1",

        """¿En qué redes sociales tuvo lugar lo sucedido?"""
        : "utter_plataforma_redes_v2",

        """¿A través de qué espacio digital sucedió el incidente?"""
        : "utter_plataforma_redes_v3",

        """¿Cuándo ocurrió lo sucedido? Puede ser una fecha y hora específicos o un período aproximado."""
        : "utter_fecha_redes_v1",

        """¿En qué fecha o período tuvo lugar lo que pasó en redes? Si no lo recuerdas bien puedes darme datos aproximados."""
        : "utter_fecha_redes_v2",

        """¿Fueron una o varias las cuentas que participaron en lo sucedido?"""
        : "utter_num_agresores_redes",

        """¿Recuerdas el nombre de usuario, correo o perfil del agresor en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: ¿sabías si esta cuenta seguía o estaba vinculada a grupos o páginas con ideologías de odio o compartía contenido de odio?"""
        : "utter_pregunta_cuenta_agresor_vinculacion_redes_v1",

        """¿Recuerdas el nombre de usuario, correo o perfil del agresor en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: a veces los perfiles comparten contenido o usan imágenes de perfil o nombres relacionados con grupos extremistas. ¿Viste algo así?"""
        : "utter_pregunta_cuenta_agresor_vinculacion_redes_v2",

        """¿Recuerdas los nombres de usuario, correos o perfiles de los agresores en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: ¿sabías si estas cuentas seguían o estaban vinculadas a grupos o páginas con ideologías de odio o compartían contenido de odio?"""
        : "utter_pregunta_cuenta_agresores_vinculacion_redes_v1",

        """¿Recuerdas los nombres de usuario, correos o perfiles de los agresores en la red social? (ej: @usuario, nombre en Facebook...) Si no te acuerdas no pasa nada, pero quizás puedas compartir detalles que son muy útiles para mí, por ejemplo: a veces los perfiles comparten contenido o usan imágenes de perfil o nombres relacionados con grupos extremistas. ¿Viste algo así?"""
        : "utter_pregunta_cuenta_agresores_vinculacion_redes_v2",

        """Cuando quieras puedes empezar a contarme lo que te ha pasado. Para que todo sea más fácil, trata de seguir el orden en que ocurrió el incidente y, si puedes, reproduce mensajes o imágenes tal como las recuerdas."""
        : "utter_invita_relato_hechos_v1",

        """Este es un espacio seguro. Puedes contar todo lo que recuerdes sobre el incidente. Será todo más fácil si me lo cuentas en orden, incluyendo los mensajes o publicaciones, y describiendo cualquier contenido que te parezca relevante."""
        : "utter_invita_relato_hechos_v2",

        """Gracias por compartir todo esto conmigo. Si hay algo más que recuerdes y te gustaría añadir, puedes hacerlo ahora. Antes de que continuemos, me gustaría hacerte una pregunta más. ¿Crees que hubo algún motivo detrás de la agresión o el comportamiento de esa persona?"""
        : "utter_invita_relato_adicional_motivacion_v1",

        """Lo que has contado hasta ahora es importante. Si sientes que quedó algo fuera o recuerdas algún otro detalle, puedes compartirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que el agresor actuó así?"""
        : "utter_invita_relato_adicional_motivacion_v2",

        """Agradezco que hayas compartido tu relato. Si se te ocurre algo más que quieras contar, puedes añadirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que el agresor actuó así?"""
        : "utter_invita_relato_adicional_motivacion_v3",

        """Gracias por compartir todo esto conmigo. Si hay algo más que recuerdes y te gustaría añadir, puedes hacerlo ahora. Antes de que continuemos, me gustaría hacerte una pregunta más. ¿Crees que hubo algún motivo detrás de la agresión o el comportamiento de esas personas?"""
        : "utter_invita_relato_adicional_motivacion_plural_v1",

        """Lo que has contado hasta ahora es importante. Si sientes que quedó algo fuera o recuerdas algún otro detalle, puedes compartirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que los agresores actuaron así?"""
        : "utter_invita_relato_adicional_motivacion_plural_v2",

        """Agradezco que hayas compartido tu relato. Si se te ocurre algo más que quieras contar, puedes añadirlo ahora. Me gustaría preguntarte una cosa antes de que continuemos. ¿Te parece que había alguna razón específica por la que los agresores actuaron así?"""
        : "utter_invita_relato_adicional_motivacion_plural_v3"
    }
}
