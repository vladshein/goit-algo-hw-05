# goit-algo-hw-05
В цій роботі було виконане порівняння трьох алгоритмів пошуку підстроки в тексті:
Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа. Були протестовані два сценарія
(з дійсною та відсутнею строкою в тексті) на двох наборах даних.

Результати.
Пошук дійсної підстроки:
Найшвидшим виявився алгоритм Кнута-Морріса-Пратта,
другим Рабіна-Карпа і повільнішим Боєра-Мура на першому наборі даних.
Перший набір даних:
==================================
Execution time of boyer_moore_search in article 1: 0.8320775999964098 seconds
Execution time of kmp_search in article 1: 0.057667100001708604 seconds
Execution time of rabin_karp_search in article 1: 0.12221739999949932 seconds
==================================
На другому наборі даних ситуація дещо змінилася.
Другий набір даних:
==================================
Execution time of boyer_moore_search in article 2: 0.01076420000026701 seconds
Execution time of kmp_search in article 2: 0.06948669999837875 seconds
Execution time of rabin_karp_search in article 2: 0.24751950000063516 seconds
==================================
Алгоритм Боєра-Мура відпрацював швидше за всіх, а Робіна-Карпа став найповільнішим.

Під час пошуку відсутньої підстроки для обох наборів даних алгоритми проявили себе
наступним чином: найшвидший Боєра-Мура, КМП на другому місці та Рабіна-Карпа останній.
Набір даних стаття 1
==================================
Execution time boyer_moore_search in article 1 of absent string: 0.0070907999979681335 seconds
Execution time of kmp_search in article 1 of absent string: 0.04270169999654172 seconds
Execution time of rabin_karp_search in article 1 of absent string: 0.1847230999992462 seconds
==================================
Набір даних стаття 2
Execution time of boyer_moore_search in article 2 of absent string: 0.00940940000145929 seconds
Execution time of kmp_search in article 2 of absent string: 0.06397540000034496 seconds
Execution time of rabin_karp_search in article 2 of absent string: 0.2260623000038322 seconds
==================================